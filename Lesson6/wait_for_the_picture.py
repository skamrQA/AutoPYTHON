from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


waiting = WebDriverWait(driver, 40).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.lead"), "Done!")
)

src = driver.find_element(By.CSS_SELECTOR, 'img[id="award"]').get_attribute("src")
print(src)

driver.quit()

