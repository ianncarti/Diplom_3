import allure
from locators import Locators
from pages.base_page import BasePage
from urls import AppUrls


class PasswordResetPage(BasePage):

    @allure.step("Открытие страницы логина")
    def open_login_page(self):
        self.open_url(AppUrls.LOGIN_PAGE)

    @allure.step("Открытие страницы восстановления пароля")
    def open_password_reset_page(self):
        self.open_url(AppUrls.PASSWORD_RESET)

    @allure.step("Нажатие ссылки 'восстановления пароля'")
    def click_password_recovery_link(self):
        self.wait_for_element_is_visible(Locators.PASSWORD_RECOVERY_LINK)
        self.click_element(Locators.PASSWORD_RECOVERY_LINK)

    @allure.step("Нажатие кнопки 'восстановить пароль'")
    def click_recover_button(self):
        self.click_element(Locators.PASSWORD_RESET_BUTTON)

    @allure.step("Ввод email")
    def input_email_for_password_reset(self, email):
        self.send_keys(Locators.EMAIL_INPUT, email)

    @allure.step("Ввод нового пароля")
    def input_new_password(self, new_password):
        self.send_keys(Locators.NEW_PASSWORD_INPUT, new_password)

    @allure.step("Нажатие кнопки показать\скрыть пароль")
    def show_hidden_password(self):
        self.wait_for_element_is_clickable(Locators.SHOW_OR_HIDE_PASSWORD_BUTTON)
        self.click_element(Locators.SHOW_OR_HIDE_PASSWORD_BUTTON)

    @allure.step("Введение нового пароля и нажатие кнопки показать\скрыть пароль")
    def fill_new_password_and_show_symbols(self, new_password):
        self.input_new_password(new_password)
        self.show_hidden_password()
