import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Завершение работы драйвера
    driver.quit()

# Функция для запуска теста
def test_submit_form():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    # Открытие сайта
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    

    # Заполнение формы
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

    # Нажатие кнопки Submit
    driver.find_element(By.TAG_NAME, "button").click()


    # Проверки (asserts)
    assert "alert py-2 alert-danger" in driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class"), "Zip code field is not highlighted in red."
    for field_id in ["first-name",
                     "last-name",
                     "address",
                     "e-mail",
                     "phone",
                     "city",
                     "country",
                     "job-position",
                     "company"]:
        assert "alert py-2 alert-success" in driver.find_element(By.ID, field_id).get_attribute("class"), f"{field_id} field is not highlighted in green."

    # Закрытие браузера после теста
    driver.quit()

# Запуск теста, если скрипт запущен напрямую
if __name__ == "__main__":
    pytest.main()