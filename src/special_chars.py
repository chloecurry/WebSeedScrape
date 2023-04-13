import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver  # idk if i need both of these imports
from selenium.webdriver.common.by import By
from lxml import html
import requests
import pandas as pd

# The goal here is to get a list of all the seeds with the following special characteristics:
# - Heirloom
# - Pollinator attractant
# - Container friendly
# - Open Pollinated
# - Nitrogen fixer


file = open("..\data\\seed_names.txt", "r")
seeds = file.read()

seedList = seeds.split("\n")

heirloomURL = "https://www.westcoastseeds.com/collections/seeds?filters%5Bcustom_fields.all_filters%5D%5B0%5D=Heirloom"
opURL = "https://www.westcoastseeds.com/collections/seeds?filters%5Bcustom_fields.all_filters%5D%5B0%5D=Open%20Pollinated"
containerFriendlyURL = "https://www.westcoastseeds.com/collections/seeds?filters%5Bcustom_fields.all_filters%5D%5B0%5D=Good%20For%20Containers"
pollinatorsURL = "https://www.westcoastseeds.com/collections/seeds?filters%5Bcustom_fields.all_filters%5D%5B0%5D=Attracts%20Pollinators"
nitrogenFixerURL = "https://www.westcoastseeds.com/collections/seeds?filters%5Bcustom_fields.all_filters%5D%5B0%5D=Nitrogen%20Fixer"

sp_chars_urls = [heirloomURL, opURL, containerFriendlyURL, pollinatorsURL, nitrogenFixerURL]

driver = webdriver.Chrome()

special_characteristics = {"Name": seedList, "Heirloom": [], "Open Pollinated": [], "Container Friendly": [], "Pollinator Attractant": [], "Nitrogen Fixer": []}

i = 0

while i < len(sp_chars_urls):

    driver.get(sp_chars_urls[i])

    characteristic = list(special_characteristics.keys())[i+1]

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
        exists = len(driver.find_elements(By.XPATH, '//a[.//h3[contains(text(), "%s")]]' %seed))
        special_characteristics[characteristic].append(exists)

    i+=1

sc_df = pd.DataFrame.from_dict(special_characteristics)

sc_df.to_excel("..\data\\special_chars.xlsx", sheet_name="cri")
    

    

