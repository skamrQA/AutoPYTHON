from Lesson7.step2.pages.FormMainPage import MainPage
from Lesson7.conftest import *

def test_submit_form(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.set_cookie_policy()
    main_page.submit_form()
    main_page.check()

