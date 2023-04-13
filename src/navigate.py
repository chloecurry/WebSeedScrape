import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver #idk if i need both of these imports
from selenium.webdriver.common.by import By

# Uses selenium webdrivers to search for all seeds via the search button on the WCS website. 
# Please note that notFOundList functionality does not work - seeds that aren't found will not be added to this list, and will need
# to be found manually

def navigate(seedList):
    driver = webdriver.Chrome()
    result_dict = {}
    urlList = []
    notFoundList = []

    for seed in seedList:
        try:
            driver.get("https://www.westcoastseeds.com/collections/seeds")
            time.sleep(1)
            
            search_button = driver.find_element(By.XPATH, '//*[@id="nav-search"]/button')
            search_button.click()
            time.sleep(1)
            search_bar = driver.find_element(By.XPATH, '//*[@id="Search"]')
            search_bar.send_keys(seed)
            search_bar.submit()

            time.sleep(2)

            seedElem = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/ul/li[1]/a')
            seedElem.click()
            geturl = driver.current_url
            urlList.append(geturl)

        except Exception as e:
            notFoundList.append(seed)

    result_dict["found"] = urlList
    result_dict["notFound"] = notFoundList

    return result_dict
    
    

