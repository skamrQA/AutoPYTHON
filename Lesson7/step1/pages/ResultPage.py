from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait	
from selenium.webdriver.support import expected_conditions as EC	

class ResultPage:

    def __init__(self, browser):
        self._driver = browser

    def swich_to_table(self):
    # Переключиться на таблицу
        self._driver.find_element(By.CSS_SELECTOR, 'a[title="таблицей"]').click
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located( (By.CSS_SELECTOR, "table") )
        )
    
    def add_books(self):
    # Добавить все книги нaа первой странице в корзину и посчитать
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1
        return counter
    
    def get_empty_result_message(self):
        #вернуть сообщение при пустом результате
        div = self._driver.finde_element(By.CSS_SELECTOR, 'div.search-error')
        h1 = div.finde_element(By.CSS_SELECTOR, 'h1')
        return h1.text