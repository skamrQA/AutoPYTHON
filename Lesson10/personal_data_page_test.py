import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from page.persDataPage import PersonalDataPage

@allure.title("Заполнить персональные данные")
@allure.description("Тест проверяет работу формы с заполнением персональных данных")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_form_elements():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной, которая хранит экзампляр класса PersonalDataPage"):
        personal_data_page = PersonalDataPage(driver)

    personal_data_page.personal_data("Кирилл", "Кириддов", "Сморенский пер-к", "skamrtest@gmail.com", "+79956541233", "Тверь", "Россия", "QA49.0", "SkyPro")
    personal_data_page.zip_code_red()
    personal_data_page.other_fields_green()
    personal_data_page.close_driver()