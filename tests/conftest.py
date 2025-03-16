import pytest
import requests
from helpers import generate_uniq_creds
from locators import Locators
from urls import AppUrls, AppUrlsApi
from webdriver_factory import WebdriverFactory
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def browser(request):
    # driver = WebdriverFactory.get_webdriver('firefox')
    # yield driver
    # driver.quit()
    browser_name = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser_name)  # Создаем WebDriver
    yield driver  # Передаем WebDriver в тест
    driver.quit()  # Закрываем браузер после завершения теста`

@pytest.fixture
def create_login_delete_account():
    valid_creds = generate_uniq_creds() #генерируем уникальные email, password, name

    response_create = requests.post(AppUrlsApi.USER_CREATE_URL, data=valid_creds) #создаём акк

    #токен и тело запроса для логина
    token = response_create.json()['accessToken']
    auth_data = {
        "email": valid_creds['email'],
        "password": valid_creds['password']
    }

    #логин
    response_login = requests.post(AppUrlsApi.LOGIN_URL, data=auth_data, headers={'accessToken': token})

    yield valid_creds, response_create, response_login, token

    requests.delete(AppUrlsApi.USER_INFO_URL, headers={'authorization': token}) #удаление акка после тестов

@pytest.fixture
def login(browser, create_login_delete_account):
    valid_creds, _, __, ___ = create_login_delete_account

    email = valid_creds['email']
    password = valid_creds['password']
    driver = browser
    driver.get(AppUrls.LOGIN_PAGE)
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*Locators.BUTTON_AUTH).click()

@pytest.fixture
def create_order(browser, create_login_delete_account, login):
    driver = browser
    # перетаскиваем булку в заказ
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FIRST_BUN_INGREDIENT))
    source_element = driver.find_element(*Locators.FIRST_BUN_INGREDIENT)
    target_element = driver.find_element(*Locators.CONSTRUCTOR_BASKET_TOP)
    # JavaScript для перетаскивания
    driver.execute_script(
        "function createEvent(typeOfEvent) { " +
        "var event = document.createEvent('CustomEvent'); " +
        "event.initCustomEvent(typeOfEvent, true, true, null); " +
        "event.dataTransfer = { " +
        "data: {}, " +
        "setData: function(key, value) { this.data[key] = value; }, " +
        "getData: function(key) { return this.data[key]; } " +
        "}; " +
        "return event; " +
        "} " +
        "function dispatchEvent(element, typeOfEvent, event) { " +
        "if (element.dispatchEvent) { " +
        "element.dispatchEvent(event); " +
        "} else if (element.fireEvent) { " +
        "element.fireEvent('on' + typeOfEvent, event); " +
        "} " +
        "} " +
        "function simulateHTML5DragAndDrop(element, destination) { " +
        "var dragStartEvent = createEvent('dragstart'); " +
        "dispatchEvent(element, 'dragstart', dragStartEvent); " +
        "var dropEvent = createEvent('drop'); " +
        "dispatchEvent(destination, 'drop', dropEvent); " +
        "var dragEndEvent = createEvent('dragend'); " +
        "dispatchEvent(element, 'dragend', dragEndEvent); " +
        "} " +
        "simulateHTML5DragAndDrop(arguments[0], arguments[1]);",
        source_element,
        target_element
    )

    # жмём кнопку оформить заказ
    button_order = driver.find_element(*Locators.CREATE_ORDER_BUTTON)
    driver.execute_script("arguments[0].click();", button_order)

    # ждём появления попапа успешного заказа
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.SUCCESS_ORDER_POPUP))

    initial_id = '9999'

    # ждём пока id заказа перестанет равнятся initial_id
    WebDriverWait(driver, 15).until(lambda driver_wait: driver.find_element(*Locators.ORDER_ID).text != initial_id)

    # запоминаем номер заказа
    order_id = driver.find_element(*Locators.ORDER_ID).text

    # ждём видимость и кликабельность кнопки закрытия попапа
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.CLOSE_SUCCESS_ORDER_BUTTON))
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.CLOSE_SUCCESS_ORDER_BUTTON))

    # закрываем попап кликом на крестик
    close_popup_button = driver.find_element(*Locators.CLOSE_SUCCESS_ORDER_BUTTON)
    driver.execute_script("arguments[0].click();", close_popup_button)

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
