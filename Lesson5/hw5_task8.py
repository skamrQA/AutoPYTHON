#открыть страничку в Chrome 
from selenium import webdriver 
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login")

driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys("testQA")

driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys("NoWayPassword")

driver.find_element(By.CSS_SELECTOR, 'i.fa').click()
sleep(2)
driver.quit()
