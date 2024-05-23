from Lesson7.step3.pages.MainPage import CalcMain


def test_slow_calculator_assert(chrome_browser):
    calcmain = CalcMain(chrome_browser)
    calcmain.slow_calc()
    calcmain.click_button()
