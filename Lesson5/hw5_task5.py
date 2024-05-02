#открыть страничку в Хром 
from selenium import webdriver 
from time import sleep

from selenium.webdriver.chrome.service import Service as ChromeService 

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
Add_Element = 'button.btn-primary'
click= driver.find_element(By.CSS_SELECTOR, Add_Element)

# Трижды кликнуть по синей кнопке 
for n in range(3):
	click.click() 
	a = driver.switch_to.alert.accept() 
	sleep(1)
sleep(5)
driver.quit()

# открыть страницу в FireFox 
# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.get("http://uitestingplayground.com/dynamicid/")

# Add_Element = 'button.btn-primary'
# click= driver.find_element(By.CSS_SELECTOR, Add_Element)

# # Трижды кликнуть по синей кнопке 
# for n in range(3):
# 	click.click() 
# 	a = driver.switch_to.alert.accept() 
# 	sleep(1)
# sleep(5)
# driver.quit()