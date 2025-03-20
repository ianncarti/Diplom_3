import allure
from locators import Locators
from pages.base_page import BasePage
from urls import AppUrls


class PersonalAccountPage(BasePage):

    @allure.step("Открытие стартовой страницы")
    def open_starting_page(self):
        self.open_url(AppUrls.MAIN_URL)

    @allure.step("Открытие страницы логина")
    def open_login_page(self):
        self.open_url(AppUrls.LOGIN_PAGE)

    @allure.step("Введение кредов и нажатие кнопки 'Войти'")
    def insert_creds_and_click_login_button(self, email, password):
        self.send_keys(Locators.EMAIL_FIELD, email)
        self.send_keys(Locators.PASSWORD_FIELD, password)
        self.click_element(Locators.BUTTON_AUTH)

    @allure.step("Логин в аккаунт")
    def login_into_personal_account(self, email, password):
        self.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        self.insert_creds_and_click_login_button(email, password)
        self.wait_for_url(AppUrls.MAIN_URL)
        self.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_for_url(AppUrls.PERSONAL_ACCOUNT)

    @allure.step("Переход в историю заказов")
    def redirect_to_order_history(self, email, password):
        self.login_into_personal_account(email, password)
        self.wait_for_element_is_visible(Locators.ORDER_HISTORY_BUTTON)
        self.click_element(Locators.ORDER_HISTORY_BUTTON)

    @allure.step("Вход и выход из аккаунта")
    def login_and_logout(self, email, password):
        self.login_into_personal_account(email, password)
        self.wait_for_element_is_visible(Locators.LOGOUT_BUTTON)
        self.click_element(Locators.LOGOUT_BUTTON)
        self.wait_for_url(AppUrls.LOGIN_PAGE)
