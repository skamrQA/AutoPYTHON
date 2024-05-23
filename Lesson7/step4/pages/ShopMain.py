from selenium.webdriver.common.by import By
from Lesson7.constants import Shop_URL

class ShopMainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Shop_URL)

    # Вход как пользователь standard_user
    def sing_in(self):
        self.browser.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys("standard_user")
        self.browser.find_element(By.CSS_SELECTOR, 'input#password').send_keys("secret_sauce")
        self.browser.find_element(By.CSS_SELECTOR, 'input#login-button').click()
    
    # Добавление товаров в корзину
    def item_addition(self):
        self.browser.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-backpack']").click()
        self.browser.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        self.browser.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-onesie']").click()

    # Переход в корзину
    def into_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()