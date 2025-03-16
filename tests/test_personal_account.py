import allure
from pages.personal_account_page import PersonalAccountPage
from urls import AppUrls


class TestPersonalAccount:

    @allure.title("Переход в личный кабинет")
    def test_personal_account_redirect_to_personal_account(self, browser, create_login_delete_account):
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.open_starting_page()
        valid_creds, _, __, ___ = create_login_delete_account
        email = valid_creds['email']
        password = valid_creds['password']
        personal_account_page.login_into_personal_account(email, password)

        assert browser.current_url == AppUrls.PERSONAL_ACCOUNT

    @allure.title("Переход в историю заказов")
    def test_personal_account_redirect_to_order_history(self, browser, create_login_delete_account):
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.open_starting_page()
        valid_creds, _, __, ___ = create_login_delete_account
        email = valid_creds['email']
        password = valid_creds['password']
        personal_account_page.redirect_to_order_history(email, password)

        assert browser.current_url == AppUrls.ORDER_HISTORY

    @allure.title("Выход из аккаунта")
    def test_personal_account_logout(self, browser, create_login_delete_account):
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.open_starting_page()
        valid_creds, _, __, ___ = create_login_delete_account
        email = valid_creds['email']
        password = valid_creds['password']
        personal_account_page.login_and_logout(email, password)

        assert browser.current_url == AppUrls.LOGIN_PAGE
