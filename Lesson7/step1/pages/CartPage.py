from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, browser):
        self._driver = browser

    def go_to_cart(self):
    # Перейти в корзину
        self._driver.get("https://www.labirint.ru/cart/")

    def get_cart_counter(self):
        # Проверить счетчик товаров. Должен быть равен числу нажатий
        # Получить текущее значение
        txt = self._driver.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]').find_element(By.CSS_SELECTOR, 'b').text
        return int(txt)
