import allure
import pytest
from locators import Locators
from pages.constructor_page import ConstructorPage
from urls import AppUrls


class TestConstructor:

    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('Открываем страницу авторизации и переходим в конструктор')
    def test_constructor_redirect_to_constructor(self, browser):
        constructor_page = ConstructorPage(browser)
        constructor_page.open_login_page()
        constructor_page.click_constructor_button()

        assert browser.current_url == AppUrls.MAIN_URL

    @allure.title("Переход в ленту заказов")
    def test_constructor_redirect_to_order_feed(self, browser):
        constructor_page = ConstructorPage(browser)
        constructor_page.open_constructor_page()
        constructor_page.click_order_feed_button()

        assert browser.current_url == AppUrls.ORDER_FEED

    @allure.title("Появление модального окна ингредиента")
    @allure.description('Кликаем на ингредиент и проверяем видимость модального окна')
    def test_constructor_ingredient_popup_is_visible(self, browser):
        constructor_page = ConstructorPage(browser)
        constructor_page.open_constructor_page()
        constructor_page.click_bun_ingredient()

        assert constructor_page.check_element_is_visible(Locators.INGREDIENT_POPUP_TITLE)

    @allure.title("Закрытие модального окна ингредиента")
    def test_constructor_close_ingredient_popup(self, browser):
        constructor_page = ConstructorPage(browser)
        constructor_page.open_constructor_page()
        constructor_page.open_and_close_ingredient_popup()

        assert constructor_page.check_element_is_visible(Locators.INGREDIENT_POPUP_TITLE) == False

    @allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
    @allure.description('Перетаскиваем булку в верхнее/нижнее поле заказа, и проверяем, что счётчик увеличился')
    @pytest.mark.parametrize('constructor_basket', (Locators.CONSTRUCTOR_BASKET_TOP, Locators.CONSTRUCTOR_BASKET_BOTTOM))
    def test_constructor_drag_and_drop_increases_counter(self, browser, constructor_basket):
        constructor_page = ConstructorPage(browser)
        constructor_page.open_constructor_page()
        constructor_page.drag_and_drop_ingredient(Locators.FIRST_BUN_INGREDIENT, constructor_basket)

        assert constructor_page.get_element_text(Locators.FIRST_BUN_COUNTER) == "2"

    @allure.title("Создание заказа авторизованным пользователем")
    @allure.description("Логинимся в аккаунт, жмём кнопку заказа, проверяем видимость id заказа")
    def test_constructor_create_order_with_auth(self, browser, login):
        constructor_page = ConstructorPage(browser)
        constructor_page.click_create_order_button()
        constructor_page.wait_for_order_id_in_popup()

        assert constructor_page.check_element_is_visible(Locators.ORDER_ID_HEADER)
