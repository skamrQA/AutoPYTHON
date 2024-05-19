from time import sleep
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    # Открываем страницу
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Вводим значение в поле с задержкой
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    sleep(1)
    delay_input.click()
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем на кнопки 7, +, 8, =
    buttons_to_click = ["7", "+", "8", "="]

    for button_text in buttons_to_click:
        buttons = browser.find_elements(By.TAG_NAME, "span")
        for button in buttons:
            if button.text == button_text:
                button.click()

    
    # Проверяем результат через 45 секунд
    time.sleep(45)
    result_element = browser.find_element(By.CSS_SELECTOR, "div.screen")
    result_value = result_element.text
    
    assert result_value == "15"
# Запуск теста, если скрипт запущен напрямую
if __name__ == "__main__":
    pytest.main()