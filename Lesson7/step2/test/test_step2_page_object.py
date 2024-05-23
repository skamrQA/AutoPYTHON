import pytest	
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from pages.MainPage import MainPage

@pytest.fixture(scope="module")
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Завершение работы драйвера
    driver.quit()

def test_submit_form():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.submit_form()
    main_page.check()

    browser.quit()

if __name__ == "__main__":
    pytest.main()