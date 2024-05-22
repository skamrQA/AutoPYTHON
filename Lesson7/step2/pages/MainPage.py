class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html") # Открытие сайта
        self._driver.implicitly_wait(4) #WebDriver будет ждать до 4 секунд, прежде чем выбросить исключение
        self._driver.maximize_window() #Максимизирует окно браузера.

    def set_cookie_policy(self):
        cookie = {
            "name": "cookie_policy", 
            "value": "1"
        }
        self._driver.add_cookie(cookie)

    def submit_form(self):
        # Заполнение формы
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
        # Zip code оставляем пустым
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")
        # Нажатие кнопки Submit
        self._driver.find_element(By.TAG_NAME, "button").click()

    def check(self):
            # Проверки (asserts)
        assert "alert py-2 alert-danger" in self._driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class"), "Zip code field is not highlighted in red."
        for field_id in ["first-name",
                     "last-name",
                     "address",
                     "e-mail",
                     "phone",
                     "city",
                     "country",
                     "job-position",
                     "company"]:
              assert "alert py-2 alert-success" in self._driver.find_element(By.ID, field_id).get_attribute("class"), f"{field_id} field is not highlighted in green."
