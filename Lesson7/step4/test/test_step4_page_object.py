from Lesson7.step4.pages.ShopMain import ShopMainPage
from Lesson7.step4.pages.Shopordering import ShopOrdering


def test_shop(chrome_browser):
    expected_total = "58.29"

    shopmain = ShopMainPage(chrome_browser)
    shopmain.sing_in()
    shopmain.item_addition()
    shopmain.into_cart()

    cart = ShopOrdering(chrome_browser)
    cart.checkout()
    cart.fill_in()
    cart.check_quit()

    assert expected_total in cart.check_quit
    print(f"Итоговая сумма равна ${cart.check_quit()}")