import scrapy
import json
from urllib.parse import urlencode

import datetime
import logging

# Set up logger once at module level to prevent handler accumulation
_url_logger = logging.getLogger(f"{__name__}.url_logger")
_url_logger.setLevel(logging.INFO)
if not _url_logger.handlers:
    _handler = logging.FileHandler('sauto_spider.log')
    _handler.setLevel(logging.INFO)
    _handler.setFormatter(logging.Formatter('%(message)s'))
    _url_logger.addHandler(_handler)


def log_url(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        for request in result:
            _url_logger.info(f"Date: {datetime.datetime.now()}, scraping url: {request.url}")
            yield request
    return wrapper

class SautoSpider(scrapy.Spider):
    """
    A scrapy spider used to scrape data from the website "https://www.sauto.cz".
    It reads parameters from a JSON file and sends HTTP GET requests to the API endpoint with different price ranges.
    The responses are parsed as JSON and the results are yielded.
    """

    name = "sauto"
    BASE_URL = "https://www.sauto.cz/api/v1/items/search?"

    @staticmethod
    def read_params_from_json(file_path: str) -> dict:
        """
        Read parameters from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The parameters read from the JSON file.
        """
        with open(file_path, "r") as file:
            params = json.load(file)
        return params

    @log_url
    def start_requests(self):
        """
        Read parameters from a JSON file, generate URLs with different price ranges,
        send HTTP GET requests, and yield the responses.
        """
        params = self.read_params_from_json("params.json")
        urls = self.generate_urls(params)

        for url in urls:
            yield scrapy.Request(url=url, method='GET', callback=self.parse, errback=self.handle_error)
            self.logger.info(f"Scraping url: {url}")

    def generate_urls(self, params: dict) -> list:
        """
        Generate URLs with different price ranges.
        Price range can be configured via params.json:
        - price_max: Maximum price (None or omitted for unlimited)
        - price_step: Price increment step (default: 200000)
        - price_from: Starting price (default: 0)
        - price_to: Ending price (if set, overrides price_max)

        Args:
            params (dict): The parameters for the API request.

        Returns:
            list: The generated URLs.
        """
        urls = []
        
        # Extract price configuration
        price_from = int(params.pop("price_from", 0))
        price_step = int(params.pop("price_step", 200000))
        price_max = params.pop("price_max", None)
        price_to = params.pop("price_to", None)
        
        # Handle JSON null values (can be None or string "null")
        if price_max is None or (isinstance(price_max, str) and price_max.lower() == "null"):
            price_max = None
        if price_to is None or (isinstance(price_to, str) and price_to.lower() == "null"):
            price_to = None
        
        # If price_to is explicitly set, use single range
        if price_to is not None:
            params_copy = params.copy()
            params_copy["price_from"] = str(price_from)
            params_copy["price_to"] = str(int(price_to))
            url = f"{self.BASE_URL}{urlencode(params_copy)}"
            urls.append(url)
            return urls
        
        # Generate multiple price ranges
        if price_max is None:
            # Unlimited: generate ranges until we hit a reasonable maximum
            # Use a very high number as practical limit (e.g., 50 million)
            price_max = 50000000
            self.logger.info("No price_max specified, using unlimited range up to 50,000,000 CZK")
        else:
            price_max = int(price_max)
        
        # Generate price ranges
        current_price = price_from
        while current_price < price_max:
            params_copy = params.copy()
            params_copy["price_from"] = str(current_price)
            params_copy["price_to"] = str(min(current_price + price_step, price_max))
            url = f"{self.BASE_URL}{urlencode(params_copy)}"
            urls.append(url)
            current_price += price_step
        
        return urls

    def parse(self, response):
        """
        Parse the JSON response and yield the results.

        Args:
            response (scrapy.http.Response): The HTTP response.

        Yields:
            dict: The parsed results.
        """
        try:
            data = json.loads(response.body)
            yield from data.get("results", [])
        except json.JSONDecodeError:
            self.logger.error("Failed to parse the response")

    def handle_error(self, failure):
        """
        Handle failed requests after all retries are exhausted.

        Args:
            failure (twisted.python.failure.Failure): The failure object containing error details.
        """
        request = failure.request
        self.logger.error(f"Request failed: {request.url}, Error: {failure.value}")