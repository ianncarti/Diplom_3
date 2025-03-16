import allure
from data import VALID_EMAIL, NEW_PASSWORD_FOR_RECOVERY
from locators import Locators
from pages.password_reset_page import PasswordResetPage
from urls import AppUrls


class TestPasswordReset:

    @allure.title("Переход на страницу восстановления пароля")
    def test_password_reset_redirect_to_password_rest_page(self, browser):
        password_reset_page = PasswordResetPage(browser)
        password_reset_page.open_login_page()
        password_reset_page.click_password_recovery_link()

        assert AppUrls.PASSWORD_FORGOT == browser.current_url

    @allure.title("Переход к форме восстановления пароля")
    def test_password_reset_input_valid_email_and_press_button(self, browser):
        password_reset_page = PasswordResetPage(browser)
        password_reset_page.open_password_reset_page()
        password_reset_page.input_email_for_password_reset(VALID_EMAIL)
        password_reset_page.click_recover_button()
        password_reset_page.wait_for_element_is_visible(Locators.MAIL_CODE_INPUT)

        assert password_reset_page.check_element_is_visible(Locators.MAIL_CODE_INPUT)

    @allure.title("Клик по кнопке показать\скрыть пароль делаем поле активным")
    def test_password_reset_show_hidden_symbols_highlights_field(self, browser):
        password_reset_page = PasswordResetPage(browser)
        password_reset_page.open_password_reset_page()
        password_reset_page.input_email_for_password_reset(VALID_EMAIL)
        password_reset_page.click_recover_button()
        password_reset_page.wait_for_element_is_visible(Locators.NEW_PASSWORD_INPUT)
        password_reset_page.fill_new_password_and_show_symbols(NEW_PASSWORD_FOR_RECOVERY)

        assert password_reset_page.check_element_is_focused(Locators.NEW_PASSWORD_INPUT)
