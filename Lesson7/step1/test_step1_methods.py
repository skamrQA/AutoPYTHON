from time import sleep	
import pytest	
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By	
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait	
from selenium.webdriver.support import expected_conditions as EC

cookie = {
    "name": "cookie_policy", 
    "value": "1"
}

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def open_labitint():
    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

def search(term):
    # Найти все книги по слову
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

def swich_to_table():
    # Переключиться на таблицу
    browser.find_element(By.CSS_SELECTOR, 'a[title="таблицей"]').click
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located( (By.CSS_SELECTOR, "table") )
    )

def add_books():
    # Добавить все книги нaа первой странице в корзину и посчитать
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    return counter

def go_to_cart():
    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    # Проверить счетчик товаров. Должен быть равен числу нажатий
    
    # Получить текущее значение
    txt = browser.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]').find_element(By.CSS_SELECTOR, 'b').text
    return int(txt)

def close_driver():
    browser.quit()
    

def test_card_counter():
    open_labitint()
    search('python')
    swich_to_table()

    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver()
    assert added == cart_counter