# sauto-scraper

## Description

This is a Scrapy-based web scraper that extracts car listings from the [sauto.cz](https://www.sauto.cz/) API. The scraper automatically queries the API with different price ranges and saves the results in JSON or CSV format for further analysis.

## Features

- Automatically generates price range queries based on configurable parameters
- Configurable search parameters via `params.json`
- Logs all scraped URLs to `sauto_spider.log`
- Outputs data in JSON or CSV format
- Uses the official sauto.cz API endpoint

## Installation

1. Clone the repository

    ```bash
    git clone https://github.com/karlosmatos/sauto-scraper.git
    cd sauto-scraper
    ```

2. Create a virtual environment (recommended)

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the requirements
    
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Modify the `params.json` file to customize your search parameters:

```json
{
    "limit": "1000",
    "offset": "0",
    "manufacturer_model_seo": "audi",
    "condition_seo": "nove,ojete,predvadeci",
    "category_id": "838",
    "operating_lease": "false",
    "price_from": "0",
    "price_step": "200000",
    "price_max": null
}
```

**Parameter Descriptions:**
- `limit`: Maximum number of results per request (must be ≤ 1000). If a price range has more results than this limit, only the first 1000 will be returned
- `offset`: Starting offset for pagination (default: "0")
- `manufacturer_model_seo`: Filter by manufacturer/model (e.g., "audi", "volkswagen", "bmw", "skoda"). Omit or set to empty string to search all manufacturers
- `condition_seo`: Filter by car condition. Common values: "nove" (new), "ojete" (used), "predvadeci" (demo). Can combine multiple with commas (e.g., "nove,ojete,predvadeci")
- `category_id`: Vehicle category ID (e.g., "838" for personal cars). Omit to search all categories
- `operating_lease`: Filter operating lease vehicles ("true" or "false")

**Price Range Configuration:**
- `price_from`: Starting price in CZK (default: 0)
- `price_step`: Price increment step in CZK (default: 200000). Smaller steps = more requests but finer granularity
  - **Important:** If a price range contains more than 1000 cars (the `limit` maximum), not all listings will be captured. Use smaller `price_step` values to ensure complete coverage
- `price_max`: Maximum price in CZK. Set to `null` for unlimited (default: null, will search up to 50,000,000 CZK)
- `price_to`: If set, uses a single price range instead of generating multiple ranges

**Note:** The spider automatically generates multiple price range queries based on these parameters. Since the API limit is 1000 results per request, ensure your `price_step` is small enough that each price range doesn't exceed this limit

### Example Configurations

**Search for Audi cars:**
```json
{
    "manufacturer_model_seo": "audi",
    "condition_seo": "nove,ojete,predvadeci",
    "price_max": "5000000"
}
```

**Search for all manufacturers (unlimited price):**
```json
{
    "manufacturer_model_seo": "",
    "price_max": null
}
```

**Search for specific price range only:**
```json
{
    "manufacturer_model_seo": "volkswagen",
    "price_from": "500000",
    "price_to": "1000000"
}
```

## Usage

### Basic Usage

Run the scraper to output JSON:

```bash
python -m scrapy crawl sauto -O data/sauto.json
```

### Output Formats

You can output in different formats:

```bash
# JSON format
python -m scrapy crawl sauto -O data/sauto.json

# CSV format
python -m scrapy crawl sauto -O data/sauto.csv

# JSON Lines format
python -m scrapy crawl sauto -O data/sauto.jl
```

### Logs

The scraper logs all scraped URLs with timestamps to `sauto_spider.log` for debugging and monitoring purposes.

## Project Structure

```
sauto-scraper/
├── sauto/
│   ├── spiders/
│   │   └── sauto_spider.py    # Main spider implementation
│   ├── items.py                # Item definitions
│   ├── pipelines.py           # Data processing pipelines
│   └── settings.py            # Scrapy settings
├── data/                       # Output directory
├── params.json                 # Search parameters configuration
├── requirements.txt            # Python dependencies
└── scrapy.cfg                  # Scrapy configuration
```

## How It Works

1. The spider reads parameters from `params.json`
2. It generates multiple API URLs with different price ranges based on `price_from`, `price_step`, and `price_max` parameters
   - Example: With `price_from=0`, `price_step=200000`, and `price_max=null`, it generates ranges: 0-200k, 200k-400k, 400k-600k, etc. (up to 50M if unlimited)
3. Each URL is queried against the sauto.cz API endpoint: `https://www.sauto.cz/api/v1/items/search?`
4. Results are parsed from JSON responses and saved to the output file
5. All URLs are logged to `sauto_spider.log` with timestamps

## License

[MIT](https://choosealicense.com/licenses/mit/)
