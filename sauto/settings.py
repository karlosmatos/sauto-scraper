# Scrapy settings for sauto project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "sauto"

SPIDER_MODULES = ["sauto.spiders"]
NEWSPIDER_MODULE = "sauto.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "sauto (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json',
    'Accept-Language': 'cs',
    'Connection': 'keep-alive',
    'Content-Type': '',
    # 'Cookie': 'appver=v1.1.350; qusnyQusny=1; szncmpone=0; seznam.cz|szncmpone=0; __cc=SnpTMWhkekZ6UVdpQWNMVjsxNzAzMDg5ODEx:THJJemVyeGFJdGsxRW15bzsxNzAzMTA0MjEx; euconsent-v2=CP3FdEAP3FdEAD3ACCCSAfEgAAAAAEPgAATIAAAQugRQAKAAsACoAFwAQAAyABoAEQAI4ATAAqgBbADEAH4AQkAiACJAEcAJwAZYAzQB3AD9AIQARYAuoBtAE2gKkAWoAtwBeYDBAGSANTAhcAAA.YAAAAAAAAAAA; ds=1YGGabLMWuACtkhq0UYX2ybeLuJ6F6am0cbZG6eeHAjwKj9tOyOGLBsvCb_alDZWTRSqRq; ps=1YGGabLMWuACtkhq0UYX2ybeLuJ6F6am0cbZG6eeHAjwKj9tOyOGLBsvCb_alDZWTRSqRq; last-redirect=1; .seznam.cz|sid=id=11340736668656664840|t=1702998056.744|te=1703078923.888|c=22891916791F2C6AA2CE1B494F07F87B; sid=id=11340736668656664840|t=1702998056.744|te=1703078923.888|c=22891916791F2C6AA2CE1B494F07F87B; sid=id=11340736668656664840|t=1702998056.744|te=1703078923.888|c=22891916791F2C6AA2CE1B494F07F87B; szncsr=1703079575; lps=eyJfZnJlc2giOmZhbHNlLCJfcGVybWFuZW50Ijp0cnVlfQ.ZYLuww.O8X5pNteFYj_ZliyXlKs_dTp5pI',
    'DNT': '1',
    'Referer': 'https://www.sauto.cz/inzerce/osobni',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'X-Szn-QQ': '1',
    'X-Xhr-Request': 'aHR0cHM6Ly93d3cuc2F1dG8uY3ovaW56ZXJjZS9vc29ibmk',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-gpc': '1',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "sauto.middlewares.SautoSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "sauto.middlewares.SautoDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "sauto.pipelines.SautoPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
