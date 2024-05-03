#открыть страничку в Chrome 
from selenium import webdriver 
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService 

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid/")

# Трижды кликнуть no синеи кнопке	
for n in range(3):
	driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
	sleep(1)
sleep(5) 
driver.quit()

# # открыть страницу в FireFox 
# from selenium import webdriver
# from webdriver.manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.get("http://uitestingplayground.com/dynamicid/")

# # Трижды кликнуть no синеи кнопке	
# for n in range(3):
# 	driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
# 	sleep(1)
# sleep(5) 
# driver.quit()