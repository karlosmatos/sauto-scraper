from pathlib import Path
from urllib.parse import urlencode

import scrapy
import json


class SautoSpider(scrapy.Spider):
    name = "sauto"

    def start_requests(self):
        cookies = {
            'appver': 'v1.1.350',
            'qusnyQusny': '1',
            'szncmpone': '0',
            'seznam.cz|szncmpone': '0',
            '__cc': 'SnpTMWhkekZ6UVdpQWNMVjsxNzAzMDg5ODEx:THJJemVyeGFJdGsxRW15bzsxNzAzMTA0MjEx',
            'euconsent-v2': 'CP3FdEAP3FdEAD3ACCCSAfEgAAAAAEPgAATIAAAQugRQAKAAsACoAFwAQAAyABoAEQAI4ATAAqgBbADEAH4AQkAiACJAEcAJwAZYAzQB3AD9AIQARYAuoBtAE2gKkAWoAtwBeYDBAGSANTAhcAAA.YAAAAAAAAAAA',
            'ds': '1YGGabLMWuACtkhq0UYX2ybeLuJ6F6am0cbZG6eeHAjwKj9tOyOGLBsvCb_alDZWTRSqRq',
            'ps': '1YGGabLMWuACtkhq0UYX2ybeLuJ6F6am0cbZG6eeHAjwKj9tOyOGLBsvCb_alDZWTRSqRq',
            'last-redirect': '1',
            '.seznam.cz|sid': 'id=11340736668656664840|t=1702998056.744|te=1703078923.888|c=22891916791F2C6AA2CE1B494F07F87B',
            'sid': 'id=11340736668656664840|t=1702998056.744|te=1703078923.888|c=22891916791F2C6AA2CE1B494F07F87B',
            'sid': 'id=11340736668656664840|t=1702998056.744|te=1703078923.888|c=22891916791F2C6AA2CE1B494F07F87B',
            'szncsr': '1703079575',
            'lps': 'eyJfZnJlc2giOmZhbHNlLCJfcGVybWFuZW50Ijp0cnVlfQ.ZYLuww.O8X5pNteFYj_ZliyXlKs_dTp5pI',
        }

        params = json.load(open("params.json", "r"))
    
        url = "https://www.sauto.cz/api/v1/items/search",
        
        for param in params:
            url = "https://www.sauto.cz/api/v1/items/search" + urlencode(param)
            yield scrapy.Request(
                url=url, 
                method='GET',
                cookies=cookies,
                callback=self.parse
            )

    def parse(self, response):
        # Save response to json file
        with open("response.json", "w") as f:
            json.dump(response.json(), f, indent=4)
