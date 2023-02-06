import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver #idk if i need both of these imports
from selenium.webdriver.common.by import By



def navigate(seedList):
    driver = webdriver.Chrome()
    result_dict = {}
    urlList = []
    notFoundList = []

    for seed in seedList:
        try:
            driver.get("https://www.westcoastseeds.com/collections/seeds")
            
            search_button = driver.find_element(By.XPATH, '//*[@id="nav-search"]/button')
            search_button.click()
            search_bar = driver.find_element(By.XPATH, '//*[@id="Search"]')
            search_bar.send_keys(seed)
            search_bar.submit()

            time.sleep(5)

            seedElem = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/ul/li[1]/a')
            driver.execute_script("arguments[0].scrollIntoView();", seedElem)
            time.sleep(2)
            seedElem.click()
            geturl = driver.current_url
            urlList.append(geturl)

        except Exception as e:
            notFoundList.append(seed)

    result_dict["found"] = urlList
    result_dict["notFound"] = notFoundList

    return result_dict
    
    

