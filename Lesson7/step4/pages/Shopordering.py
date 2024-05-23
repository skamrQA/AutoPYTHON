from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopOrdering:
    def __init__(self, browser):
        self.browser = browser

    # Нажатие кнопки Checkout
    def checkout(self):
        self.browser.find_element(By.CSS_SELECTOR, "button[id='checkout']").click()

    # Заполнение формы данными
    def fill_in(self):
        self.browser.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys("John")
        self.browser.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys("Doe")
        self.browser.find_element(By.CSS_SELECTOR, 'input#postal-code').send_keys("12345")
        self.browser.find_element(By.CSS_SELECTOR, 'input#continue').click()

    # Проверка итоговой суммы
    def check_quit(self):
        total_amount = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
        assert total_amount.text == "Total: $58.29", "Итоговая сумма не соответствует ожидаемой"
    # Закрытие браузера
        self.browser.quit()