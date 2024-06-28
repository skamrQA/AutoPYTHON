import allure
from selenium.webdriver.common.by import By

class PersonalDataPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    @allure.step("Заполнение формы персональными данными")
    def personal_data(self, name: str, last: str, address: str, email: str, phone: int, city: str, country: str, job: str, company: str):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "first-name"]').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "last-name"]').send_keys(last)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "address"]').send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "e-mail"]').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "phone"]').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "zip-code"]').clear()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "city"]').send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "country"]').send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "job-position"]').send_keys(job)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "company"]').send_keys(company)

        element = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Метод для определения, красного ли цвета поле ввода, если оно не заполнено")
    def zip_code_red(self):
        zip_code_color = self.driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        if zip_code_color is None:
           zip_code_color = "default_color" 
        return zip_code_color == 'rgba(248, 215, 218, 1)'

    @allure.step("Метод для определения, зелёного ли цвета поля ввода, если они заполнены")
    def other_fields_green(self):
        other_fields = ["#first-name", "#last-name", "#address", "#e-mail",
                        "#phone", "#city", "#country", "#job-position", "#company"]
        for field in other_fields:
            field_color = self.driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color")
            if field_color is None:
               field_color = "default_color" 
        return field_color == 'rgba(209, 231, 221, 1)'

    @allure.step("Закрытие веб-браузера")
    def close_driver(self):
        self.driver.quit()