from selenium.webdriver.common.by import By

class Locators:
    #Password reset page
    PASSWORD_RESET_BUTTON = [By.CLASS_NAME, "button_button__33qZ0"]
    PASSWORD_RECOVERY_LINK = [By.XPATH, ".//p[text()='Забыли пароль?']/a"]
    EMAIL_INPUT = [By.XPATH, ".//input"]
    NEW_PASSWORD_INPUT = [By.XPATH, ".//div/input[@name='Введите новый пароль']"]
    MAIL_CODE_INPUT = [By.XPATH, ".//label[text()='Введите код из письма']"]
    SHOW_OR_HIDE_PASSWORD_BUTTON = [By.XPATH, ".//div[contains(@class, 'input__icon')]"]

    #Main page
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, ".//p[text()='Личный Кабинет']"]

    #Login page
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # поле ввода email
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # поле ввода пароля
    BUTTON_AUTH = (By.XPATH, ".//button[text()='Войти']")  # кнопка входа в аккаунт

    #Personal account page
    LOGOUT_BUTTON = [By.XPATH, ".//button[text()='Выход']"]
    ORDER_HISTORY_BUTTON = [By.XPATH, ".//a[text()='История заказов']"]

    #Constructor page
    CONSTRUCTOR_BUTTON = [By.XPATH, ".//p[text()='Конструктор']"]
    ORDER_FEED_BUTTON = [By.XPATH, ".//p[text()='Лента Заказов']"]
    INGREDIENT_POPUP_TITLE = [By.XPATH, ".//h2[text()='Детали ингредиента']"]
    FIRST_BUN_INGREDIENT = [By.XPATH, "(.//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[1]"]
    CLOSE_INGREDIENT_POPUP_BUTTON = [By.XPATH, ".//section[1]/div[@class='Modal_modal__container__Wo2l_']/button[1]"]
    CONSTRUCTOR_BASKET_TOP = [By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]"]
    CONSTRUCTOR_BASKET_BOTTOM = [By.XPATH, ".//div[contains(@class, 'constructor-element_pos_bottom')]"]
    FIRST_BUN_COUNTER = [By.XPATH, "(.//p[@class='counter_counter__num__3nue1'])[1]"]
    CREATE_ORDER_BUTTON = [By.XPATH, ".//button[text()='Оформить заказ']"]
    ORDER_ID_HEADER = [By.XPATH, ".//p[text()='идентификатор заказа']"]
    ORDER_ID = [By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]"]
    SUCCESS_ORDER_POPUP = [By.XPATH, ".//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]"]
    CLOSE_SUCCESS_ORDER_BUTTON = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]"]

    #Order feed page
    FIRST_ORDER_IN_FEED = [By.XPATH, "(.//li[@class='OrderHistory_listItem__2x95r mb-6'])[1]"]
    ORDER_POPUP = [By.XPATH, ".//div[contains(@class, 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X')]"]
    FIRST_ORDERS_ID_IN_FEED = [By.XPATH, "(.//p[contains(@class, 'text text_type_digits-default')])[1]"]
    ALL_TIME_COUNTER = [By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p"]
    TODAY_COUNTER = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p"]
    AT_WORK_LIST = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li"]
