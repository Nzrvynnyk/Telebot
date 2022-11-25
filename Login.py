
#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import selenium
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("http://Admin:/index.htm")

time.sleep(5)
# fill in username and hit the next button
elem = driver.find_element_by_xpath('//div[25]/div[2]')
actions = ActionChains(driver)
actions.click(elem).perform()
time.sleep(2)
elm2 = driver.find_element_by_xpath('//div[26]/div[4]/div[2]')
time.sleep(2)
actions = ActionChains(driver)
actions.click(elm2).perform()
time.sleep(5)
elm3 = driver.find_element_by_xpath('//div[2]/input')
actions = ActionChains(driver)
actions.click(elm3).perform()
time.sleep(2)
#inputElement = driver.find_element_by_xpath("//input")
#inputElement.send_keys('00:1c:c0:7b:ec:66')
#inputElement.click()

#time.sleep(15)


driver.close()


if __name__ == "__main__":
