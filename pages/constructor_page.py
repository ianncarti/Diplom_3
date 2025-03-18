import allure
from locators import Locators
from pages.base_page import BasePage
from urls import AppUrls


class ConstructorPage(BasePage):

    @allure.step("Открытие страницы конструктора")
    def open_constructor_page(self):
        self.open_url(AppUrls.MAIN_URL)

    @allure.step("Открытие страницы логина")
    def open_login_page(self):
        self.open_url(AppUrls.LOGIN_PAGE)

    @allure.step("Нажатие кнопки 'Конструктр' в хэдере")
    def click_constructor_button(self):
        self.click_element(Locators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажатие кнопки 'Лента заказов' в хэдере")
    def click_order_feed_button(self):
        self.click_element(Locators.ORDER_FEED_BUTTON)

    @allure.step("Нажатие на первую булочку в ингредиентах")
    def click_bun_ingredient(self):
        self.click_element_alternate(Locators.FIRST_BUN_INGREDIENT)

    @allure.step("Закрытие модального окна с описанием ингредиента")
    def click_close_popup_button(self):
        self.click_element_alternate(Locators.CLOSE_INGREDIENT_POPUP_BUTTON)

    @allure.step("Проверка видимости модального окна после открытия и закрытия")
    def open_and_close_ingredient_popup(self):
        self.click_bun_ingredient()
        self.wait_for_element_is_clickable(Locators.CLOSE_INGREDIENT_POPUP_BUTTON)
        self.click_close_popup_button()
        self.wait_for_element_is_invisible(Locators.CLOSE_INGREDIENT_POPUP_BUTTON)

    @allure.step("Перетягивание ингредиента")
    def drag_and_drop_ingredient(self, source_locator, target_locator):
        self.drag_and_drop(source_locator, target_locator)

    @allure.step("Нажатие кнопки 'Оформить заказ'")
    def click_create_order_button(self):
        self.wait_for_element_is_visible(Locators.CREATE_ORDER_BUTTON)
        self.click_element(Locators.CREATE_ORDER_BUTTON)

    @allure.step("Ожидание видимости id заказа")
    def wait_for_order_id_in_popup(self):
        self.wait_for_element_is_visible(Locators.ORDER_ID_HEADER)

    @allure.step("Ожидание видимости первой булочки")
    def wait_for_first_bun_visibility(self):
        self.wait_for_element_is_visible(Locators.FIRST_BUN_INGREDIENT)

    @allure.step("Ожидание видимости попапа успешного заказа")
    def wait_for_success_order_popup(self):
        self.wait_for_element_is_visible(Locators.SUCCESS_ORDER_POPUP)

    def wait_for_close_button_is_visible_and_clickable(self):
        self.wait_for_element_is_visible(Locators.CLOSE_SUCCESS_ORDER_BUTTON)
        self.wait_for_element_is_clickable(Locators.CLOSE_SUCCESS_ORDER_BUTTON)

    def click_close_success_order_popup(self):
        self.click_element(Locators.CLOSE_SUCCESS_ORDER_BUTTON)
