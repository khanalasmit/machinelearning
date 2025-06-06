# Web Scraping Bots Project

This folder contains Python scripts and resources for web scraping using Selenium, including bots for Amazon and YouTube.

## Files

- **amazon_bot.py**  
  Contains the `Amazon_bot` class for automating Amazon product search, pagination, and HTML collection using Selenium.

- **youtube_bot.py**  
  Contains the `YouTube_bot` class (or similar) for automating YouTube search and data extraction using Selenium.

- **Readme.md**  
  This file. Describes the contents and usage of the folder.

- **(Any Jupyter Notebooks or scripts you create)**  
  Use these to process, parse, and analyze the HTML files collected by the bots.

## Usage

### 1. Set up Selenium and ChromeDriver  
Make sure you have Selenium installed and the appropriate ChromeDriver available in your PATH.

### 2. Run the Amazon Bot  
Import and use the `Amazon_bot` class in your script or notebook:
```python
from amazon_bot import Amazon_bot

url = 'https://www.amazon.com'
search_item = 'most expensive laptops'
bot = Amazon_bot(url, search_item)
htmls = bot.get_html()