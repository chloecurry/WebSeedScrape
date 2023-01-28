import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver #idk if i need both of these imports
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.westcoastseeds.com/collections/seeds")

#seedList = ["Touchstone Gold", "Bull\'s Blood Organic"]
seedList = ["Touchstone Gold", "Bull\'s Blood Organic", "Get Stuffed!", "Helenor (Coated) Certified Organic", "TFM", "Tres Fine Maraichere", "TFM (Tres Fine Maraichere)"]


# Get scroll height.
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to the bottom.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load the page.
    time.sleep(5)

    # Calculate new scroll height and compare with last scroll height.
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height

time.sleep(10)

for seed in seedList:
    try:
        seedElem = driver.find_element(By.XPATH, '//a[.//h3[contains(text(), "%s")]]' %seed)
        driver.execute_script("arguments[0].scrollIntoView();", seedElem)
        time.sleep(2)
        seedElem.click()
        geturl = driver.current_url
        print(geturl)
        driver.back()
    except Exception as e:
        print("seed not found: " + seed)
    
