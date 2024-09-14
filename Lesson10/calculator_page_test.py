import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from page.calculPage import CalculatorPage

@allure.title("Сложение чисел на калькуляторе")
@allure.description("Тест проверяет корректное выполнение математических задач на калькуляторе")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_form_calculator():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной, которая хранит экзампляр класса CalculatorPage"):
        calculator_page = CalculatorPage(driver)

    calculator_page.delay()
    calculator_page.sum_of_the_numbers()
    calculator_page.get_result()
    calculator_page.close_driver()