import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Функция для запуска теста
def test_submit_form():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.ID, "email").send_keys("test@skypro.com")
    driver.find_element(By.ID, "phone-number").send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.ID, "city").send_keys("Москва")
    driver.find_element(By.ID, "country").send_keys("Россия")
    driver.find_element(By.ID, "job-position").send_keys("QA")
    driver.find_element(By.ID, "company").send_keys("SkyPro")

    # Нажатие кнопки Submit
    driver.find_element(By.ID, "submit").click()

    # Ожидание, чтобы убедиться, что страница обновилась
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result")))

    # Проверки (asserts)
    assert "alert py-2 alert-danger" in driver.find_element(By.ID, "zip-code").get_attribute("class"), "Zip code field is not highlighted in red."
    for field_id in ["first-name", "last-name", "address", "email", "phone-number", "city", "country", "job-position", "company"]:
        assert "alert py-2 alert-success" in driver.find_element(By.ID, field_id).get_attribute("class"), f"{field_id} field is not highlighted in green."

    # Закрытие браузера после теста
    driver.quit()

# Запуск теста, если скрипт запущен напрямую
if __name__ == "__main__":
    pytest.main()
