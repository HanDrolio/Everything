# house_hunt_zillow_bot.py
# 🔍 Zillow Listing Scanner — Han Drolo Mode

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Zillow TX & AZ URLs (modify as needed)
ZILLOW_URLS = {
    "Texas": "https://www.zillow.com/tx/?searchQueryState={}",
    "Arizona": "https://www.zillow.com/az/?searchQueryState={}"
}

# Setup Selenium driver
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver

def scrape_zillow(state):
    print(f"🌐 Scanning listings in {state}...")
    driver = get_driver()
    driver.get(ZILLOW_URLS[state])
    sleep(5)  # wait for page to load

    listings = driver.find_elements("css selector", ".list-card-info")

    for card in listings:
        try:
            price = card.find_element("css selector", ".list-card-price").text
            address = card.find_element("tag name", "address").text
            details = card.find_elements("css selector", ".list-card-details li")
            beds = baths = 0

            for d in details:
                text = d.text
                if "bd" in text:
                    beds = int(text.split()[0])
                elif "ba" in text:
                    baths = float(text.split()[0])

            price_val = int(''.join(filter(str.isdigit, price)))
            if price_val <= 300000 and beds >= 3 and baths >= 2:
                print(f"🏡 {address} | 💲{price} | 🛏 {beds} | 🛁 {baths}")
        except:
            continue
    driver.quit()

if __name__ == "__main__":
    for state in ZILLOW_URLS:
        scrape_zillow(state)
