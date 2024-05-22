import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

# Открытие сайта магазина
driver.get("https://www.saucedemo.com/")

# Вход как пользователь standard_user
driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()

# Добавление товаров в корзину
driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-onesie']").click()

# Переход в корзину
driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

# Нажатие кнопки Checkout
driver.find_element(By.CSS_SELECTOR, "button[id='checkout']").click()

# Заполнение формы данными
driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys("John")
driver.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys("Doe")
driver.find_element(By.CSS_SELECTOR, 'input#postal-code').send_keys("12345")
driver.find_element(By.CSS_SELECTOR, 'input#continue').click()

# Проверка итоговой суммы
total_amount = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
assert total_amount.text == "Total: $58.29", "Итоговая сумма не соответствует ожидаемой"

# Закрытие браузера
driver.quit()

if __name__ == "__main__":
    pytest.main()