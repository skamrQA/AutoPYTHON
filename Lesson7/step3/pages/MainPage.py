from selenium.webdriver.common.by import By	
from selenium.webdriver.support.ui import WebDriverWait	
from selenium.webdriver.support import expected_conditions as EC
from Lesson7.constants import Calculator_URL

class CalcMain:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Calculator_URL)

    def slow_calc(self):
        delay_input = self.browser.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")
    
    def click_button(self):
        # Нажимаем на кнопки 7, +, 8, =
        buttons_to_click = ["7", "+", "8", "="]
        for button_text in buttons_to_click:
            buttons = self.browser.find_elements(By.TAG_NAME, "span")
            for button in buttons:
                if button.text == button_text:
                    button.click()