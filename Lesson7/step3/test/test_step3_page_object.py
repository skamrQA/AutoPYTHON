from Lesson7.step3.pages.CalcMainPage import CalcMain


def test_slow_calculator_assert(chrome_browser):
    calcmain = CalcMain(chrome_browser)
    calcmain.slow_calc()
    calcmain.click_button_wait()
    assert "15" in calcmain.check()
