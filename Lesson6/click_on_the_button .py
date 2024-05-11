# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("http://uitestingplayground.com/ajax")
# driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

# green_banner = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
#     )
# text = green_banner.text
# print(text)
# driver.quit()