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
    name = "sauto"
    BASE_URL = "https://www.sauto.cz/api/v1/items/search?"

    @log_url
    def start_requests(self):
        with open("params.json", "r") as file:
            params = json.load(file)

        for price in range(0, 2000001, 200000):
            params["price_from"] = price
            params["price_to"] = price + 200000 if price <= 1800000 else 0    
            url = f"{self.BASE_URL}{urlencode(params)}"
            yield scrapy.Request(url=url, method='GET', callback=self.parse)
            self.logger.info(f"Scraping url: {url}")

    def parse(self, response):
        try:
            data = json.loads(response.body)
            for item in data.get("results", []):
                yield item
        except json.JSONDecodeError:
            self.logger.error("Failed to parse the response")