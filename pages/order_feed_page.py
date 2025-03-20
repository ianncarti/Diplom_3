import allure
from data import ALL_ORDERS_DONE_TEXT
from locators import Locators
from pages.base_page import BasePage
from urls import AppUrls


class OrderFeedPage(BasePage):

    @allure.step("Открытие страницы 'Лента заказов'")
    def open_order_feed_page(self):
        self.open_url(AppUrls.ORDER_FEED)

    @allure.step("Нажатие кнопки 'Лента заказов'")
    def click_order_feed_button(self):
        self.click_element(Locators.ORDER_FEED_BUTTON)

    @allure.step("Нажатие на первый заказ в ленте заказов")
    def click_first_order_in_feed(self):
        self.wait_for_element_is_visible(Locators.FIRST_ORDER_IN_FEED)
        self.click_element_alternate(Locators.FIRST_ORDER_IN_FEED)

    @allure.step("Поиск номера заказа в ленте заказов")
    def find_order_id_in_feed(self, order_id):
        self.wait_for_element_is_visible(Locators.FIRST_ORDERS_ID_IN_FEED)
        text = self.find_text_on_page(order_id)
        return text

    @allure.step("Получить количество заказов за всё время")
    def get_all_time_counter_int(self):
        self.wait_for_element_is_visible(Locators.ALL_TIME_COUNTER)
        all_time_count = self.get_element_text(Locators.ALL_TIME_COUNTER)
        return int(all_time_count)

    @allure.step("Получить количество заказов за сегодня")
    def get_today_counter_int(self):
        self.wait_for_element_is_visible(Locators.TODAY_COUNTER)
        today_count = self.get_element_text(Locators.TODAY_COUNTER)
        return int(today_count)

    @allure.step("Получить id заказа, который находится в работе")
    def get_at_work_order_id(self):
        self.wait_for_element_is_visible(Locators.AT_WORK_LIST)
        self.wait_for_text_change(Locators.AT_WORK_LIST, ALL_ORDERS_DONE_TEXT)
        at_work_id = self.get_element_text(Locators.AT_WORK_LIST)
        return at_work_id
