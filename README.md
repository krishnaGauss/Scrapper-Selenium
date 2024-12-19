# Scrapper Selenium
This Selenium powered python script helps to scrape bestsellers data from top-10 categories and stores it in a .csv and .json file format.

### Taking Help From

- Selenium Installation : https://selenium-python.readthedocs.io/
- Selenium Docs : https://www.selenium.dev/documentation/

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Prototype Image](#prototype-image)
- [License](#license)

## Project Overview

### Objective

- Build a web scraper using **Selenium** to automate the process of extracting bestseller product information from an e-commerce website (e.g., Amazon).
- Collect essential product details such as:
  - Product Name
  - Price
  - Discount
  - Seller Information
  - Best Seller Ranking
  - Category
  - Rating
  - Product Images
  - Product Description
  - Past Month's Sale Count
- Store the scraped data in **JSON** and **CSV** formats for analysis and reporting.

### Key Features

1. **User Authentication**:
   - Automates login using provided credentials (email and password) via the `.env` file for secure storage.

2. **Bestsellers Navigation**:
   - Automatically navigates to the bestsellers page and extracts links to various product categories.

3. **Category Traversal**:
   - Collects product links from different categories and traverses through multiple pages by scrolling down.

4. **Product Data Extraction**:
   - Extracts key product details including:
     - **Product Name**
     - **Price**
     - **Discount**
     - **Seller Information**
     - **Best Seller Rank**
     - **Rating**
     - **Product Images**
     - **Description**
     - **Past Month's Sale Count**

5. **Dynamic Scrolling**:
   - Uses infinite scroll to load more products on the page as you scroll down.

6. **Data Saving**:
   - Saves the scraped data into structured **JSON** and **CSV** formats for easy access, analysis, and reporting.

## Installation

`Note` : Please make sure that you have enabled dev mode in Google Chrome and have installed chrome web driver for the same. 
You can install it for latest chrome version from : https://googlechromelabs.github.io/chrome-for-testing/

After this extract the files to `C:\webdrivers` and add the path to `PATH` in `Environment Variables`.




### Clone the Repository

```bash
git clone https://github.com/krishnaGauss/Scrapper-Selenium.git
```
### Initialise Virtual Environment

In project root directory;

```bash
python -m venv myvenv
```

Select this virtual environment as your default interpreter for this project.

Installing Packages:
```bash
pip install -r requirements.txt
```

### Creating `.env` file 
- In project root directory setup a `.env` file with the following attributes;
```text
SIGN_IN_URL = https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0
EMAIL = <Your email ID / phone number for amazon a/c>
PASSWORD = <Your amazon a/c password>
```

## Running the Application

### Running Test.py 

Since the `main.py` script searches through all the categories and downloads the links for the products it takes around 15-20 mins for completing its process.

Hence, there is a `test.py` script provided to run the whole process but on a smaller scale for testing and evaluation purposes.

In terminal; 
```bash
python test.py
```
The same step as above can be followed for running `main.py`

## Prototype Image

- Running the application
![run](/assets/run.png)

- CSV file
![run](/assets/csv.png)


- Terminal Output
![run](/assets/terminal.png)

- JSON file
![run](/assets/json.png)

## License

MIT License

Copyright (c) `2024` `Krishna Goswami`

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
