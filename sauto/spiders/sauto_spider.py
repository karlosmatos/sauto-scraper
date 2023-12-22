import scrapy
import json
from urllib.parse import urlencode

import datetime
import logging

def log_url(func):
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create a file handler
    handler = logging.FileHandler('sauto_spider.log')
    handler.setLevel(logging.INFO)

    # Add the handler to the logger
    logger.addHandler(handler)

    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        for request in result:
            # Log the URL to the file
            logger.info(f"Date: {datetime.datetime.now()}, scraping url: {request.url}")
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
            yield scrapy.Request(url=url, method='GET', callback=self.parse)
            self.logger.info(f"Scraping url: {url}")

    def generate_urls(self, params: dict) -> list:
        """
        Generate URLs with different price ranges.

        Args:
            params (dict): The parameters for the API request.

        Returns:
            list: The generated URLs.
        """
        urls = []
        for price in range(0, 2000001, 200000):
            params["price_from"] = price
            params["price_to"] = price + 200000 if price <= 1800000 else 0
            url = f"{self.BASE_URL}{urlencode(params)}"
            urls.append(url)
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
            for item in data.get("results", []):
                yield item
        except json.JSONDecodeError:
            self.logger.error("Failed to parse the response")