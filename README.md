# sauto-scraper

## Description

This is a simple scraper that uses scrapy to scrape car list from the website https://www.sauto.cz/. The scraped data can be used for further analysis.

## Installation

1. Clone the repository

    ```bash
    git clone 
    ```

2. Install the requirements
    
    ```bash
    pip install -r requirements.txt
    ```

3. Run the scraper
    
    ```bash
    scrapy crawl sauto -O data/sauto.json
    ```

## Usage

1. Run the scraper
2. The scraped data will be saved in the `data` folder

## License

[MIT](https://choosealicense.com/licenses/mit/)
