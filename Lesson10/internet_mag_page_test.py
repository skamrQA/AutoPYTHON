import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from page.inetMagPage import InternetMagPage

@allure.title("Выбор товара, работа с корзиной и оплата")
@allure.description("Тест проверяет покупку товаров в интернет-магазине")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_form_internet_mag():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной, которая хранит экзампляр класса InternetMagPage"):
        internet_mag_page = InternetMagPage(driver)

    internet_mag_page.authorization("standard_user", "secret_sauce")
    price_added = internet_mag_page.add_products()
    internet_mag_page.go_to_cart()
    internet_mag_page.personal_data("Kamil'", "Сафин", "121100")
    price_calc = internet_mag_page.total_cost()

    with allure.step("Проверить,что ожидаемая и фактическая стоимость равны"):
        assert price_calc == price_added