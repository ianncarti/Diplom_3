import pytest
import requests
from helpers import generate_uniq_creds
from locators import Locators
from pages.constructor_page import ConstructorPage
from pages.personal_account_page import PersonalAccountPage
from urls import AppUrlsApi
from webdriver_factory import WebdriverFactory
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser_name)  # Создаем WebDriver
    yield driver  # Передаем WebDriver в тест
    driver.quit()  # Закрываем браузер после завершения теста

@pytest.fixture
def create_login_delete_account():
    valid_creds = generate_uniq_creds() # Генерируем уникальные email, password, name

    response_create = requests.post(AppUrlsApi.USER_CREATE_URL, data=valid_creds) #создаём акк

    # Токен и тело запроса для логина
    token = response_create.json()['accessToken']
    auth_data = {
        "email": valid_creds['email'],
        "password": valid_creds['password']
    }

    # Логин
    response_login = requests.post(AppUrlsApi.LOGIN_URL, data=auth_data, headers={'accessToken': token})

    yield valid_creds, response_create, response_login, token

    requests.delete(AppUrlsApi.USER_INFO_URL, headers={'authorization': token}) #удаление акка после тестов

@pytest.fixture
def login(browser, create_login_delete_account):
    valid_creds, _, __, ___ = create_login_delete_account
    email = valid_creds['email']
    password = valid_creds['password']
    personal_account_page = PersonalAccountPage(browser)
    personal_account_page.open_login_page()
    personal_account_page.insert_creds_and_click_login_button(email, password)

@pytest.fixture
def create_order(browser, create_login_delete_account, login):
    constructor_page = ConstructorPage(browser)
    constructor_page.wait_for_first_bun_visibility()
    # перетягиваем булочку
    constructor_page.drag_and_drop(Locators.FIRST_BUN_INGREDIENT, Locators.CONSTRUCTOR_BASKET_TOP)
    constructor_page.click_create_order_button()
    # ждём появления попапа успешного заказа
    constructor_page.wait_for_success_order_popup()
    initial_id = '9999'
    # ждём пока id заказа перестанет равнятся initial_id
    WebDriverWait(browser, 15).until(lambda driver_wait: browser.find_element(*Locators.ORDER_ID).text != initial_id)
    # запоминаем номер заказа
    order_id = browser.find_element(*Locators.ORDER_ID).text
    # ждем видимость кнопки закрытия и нажимаем на неё
    constructor_page.wait_for_close_button_is_visible_and_clickable()
    constructor_page.click_close_success_order_popup()

    return order_id

@pytest.fixture
def get_order_counters():
    response = requests.get(AppUrlsApi.GET_ALL_ORDERS_URL)
    all_time_counter = response.json()["total"]
    today_counter = response.json()["totalToday"]
    return int(all_time_counter), int(today_counter)

def pytest_addoption(parser):
    """
    Добавляет аргумент командной строки '--browser' для выбора браузера.
    По умолчанию используется Chrome.
    """
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")
