from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import json
import pandas as pd
from dotenv import load_dotenv
import re

load_dotenv()

SIGN_IN_URL = os.getenv('SIGN_IN_URL')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

driver = webdriver.Chrome()
driver.get(SIGN_IN_URL)

try:

    time.sleep(10)
    email_field = driver.find_element(By.ID, "ap_email")
    email_field.send_keys(EMAIL)
    driver.find_element(By.ID, "continue").click()
    time.sleep(7)

    password_field = driver.find_element(By.ID, "ap_password")
    password_field.send_keys(PASSWORD)
    driver.find_element(By.ID, "signInSubmit").click()
    time.sleep(7)

    # selecting best seller
    best_seller = driver.find_element(
        By.XPATH, "//a[contains(@href, '/gp/bestsellers')]")
    best_seller.click()

    assert "bestsellers" in driver.current_url.lower(
    ), "Navigation to Best Sellers failed"
    print("Successfully navigated to Best Sellers")

    get_category_col = driver.find_element(
        By.CLASS_NAME, "_p13n-zg-nav-tree-all_style_zg-browse-group__88fbz")
    category_hrefs = get_category_col.find_elements(By.TAG_NAME, "a")

    # Extracting href tags
    cc_category_links = [link.get_attribute("href") for link in category_hrefs]
    category_links = cc_category_links[3:13]

    products = []

    for link in category_links:
        driver.get(link)
        time.sleep(2)

        while True:

            last_height = driver.execute_script(
                "return document.body.scrollHeight")
            while True:
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)

                all_prod = driver.find_elements(By.ID, "gridItemRoot")
                for elem in all_prod:
                    try:
                        prod_href = elem.find_element(
                            By.TAG_NAME, "a").get_attribute('href')
                        if prod_href not in products:
                            products.append(prod_href)
                    except:
                        continue

                new_height = driver.execute_script(
                    "return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            # "Next" button
            try:
                next_button = WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//a[contains(@class, 'pagnNext') or contains(text(),'Next')]"))
                )
                next_button.click()
                time.sleep(3)
            except:

                break

    print(f"Total products found: {len(products)}")

    data = []

    for link in products:
        # for testing purpose only
        # for link in range(10):

        driver.get(link)

        # for testing purpose only
        # driver.get(products[link])
        time.sleep(5)

        try:
            product_name = driver.find_element(
                By.ID, 'productTitle').text.strip()
        except:
            product_name = "N/A"

        try:
            price = driver.find_element(
                By.CLASS_NAME, "a-price-whole").text.strip()
        except:
            price = "N/A"

        try:
            discount = driver.find_element(
                By.CLASS_NAME, "savingsPercentage").text.strip()
        except:
            discount = "N/A"

        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)

        try:
            # seller = driver.find_element(
            #     By.XPATH, "//span[@class='a-size-small a-color-base']/a").text
            # seller = driver.find_element(By.ID, 'sellerProfileTriggerId').text
            seller_div = driver.find_element(
                By.XPATH, "//div[contains(@tabular-attribute-name,'Sold by') and contains(@class, 'tabular-buybox-text')]")
            seller_span = seller_div.get_attribute('outerHTML')

            match = re.search(
                r'<a [^>]*id="sellerProfileTriggerId"[^>]*>(.*?)</a>', seller_span)

            if match:
                seller = match.group(1).strip()
        except:
            seller = "N/A"
        try:

            ships_from_div = driver.find_element(
                By.XPATH, "//div[@class='tabular-buybox-text a-spacing-none']")
            ship_from_span = ships_from_div.get_attribute('outerHTML')

            match = re.search(r"<span[^>]*>(.*?)</span>", ship_from_span)

            if match:
                ship_from = match.group(1).strip()
        except:
            ship_from = "N/A"
        try:
            rating = driver.find_element(
                By.XPATH, "//a[@role='button']/span[@class='a-size-base a-color-base']").text.strip()
        except:
            rating = "N/A"
        try:
            image_urls = []
            images_elems = driver.find_elements(
                By.XPATH, "//div[@id='altImages']//img")
            for elems in images_elems:
                image_url = elems.get_attribute('src')
                if image_url:
                    image_urls.append(image_url)
        except:
            image_urls = "N/A"
        try:
            past_month_sale = driver.find_element(
                By.XPATH, "//span[@id='social-proofing-faceout-title-tk_bought']/span[@class='a-text-bold']").text.strip().split()[0]
        except:
            past_month_sale = "N/A"

        for _ in range(7):
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(1)

        try:
            product_description = driver.find_element(
                By.XPATH, "//div[@id='productDescription']//span").text.strip()
        except:
            product_description = "N/A"
        try:
            span_element = driver.find_element(
                By.ID, 'productDetails_detailBullets_sections1')
            best_seller_span = span_element.get_attribute('outerHTML')

            ranks = re.findall(r"#(\d+)", best_seller_span)
            best_seller_rating = ranks[0]
        except:
            best_seller_rating = "N/A"
        try:
            match = re.search(
                r"<th[^>]*> Best Sellers Rank </th>.*?<span>(.*?)</span>",
                best_seller_span,
                re.DOTALL
            )

            if match:
                category = match.group(1).strip()

            category_cleaned = re.sub(r"#\d+\s+in\s+", "", category)
            category_cleaned = re.sub(r"\(.*?\)", "", category_cleaned).strip()
            category = category_cleaned.replace("<span>", "", 1).strip()

        except:
            category = "N/A"

        data.append({
            "product_name": product_name,
            "price": price,
            "discount": discount,
            "sold_by": seller,
            "rating": rating,
            "best_seller_rating": best_seller_rating,
            "ship_from": ship_from,
            "past_month_sale": past_month_sale,
            "category": category,
            "product_description": product_description,
            "images": image_urls
        })


finally:
    driver.quit()

output_dir = "./data"
os.makedirs(output_dir, exist_ok=True)

# Convert to a JSON file
json_file_path = os.path.join(output_dir, "products.json")
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
print(f"Data saved to JSON file: {json_file_path}")

# Convert to a CSV file
csv_file_path = os.path.join(output_dir, "products.csv")
df = pd.DataFrame(data)
df.to_csv(csv_file_path, index=False, encoding="utf-8")
print(f"Data saved to CSV file: {csv_file_path}")
