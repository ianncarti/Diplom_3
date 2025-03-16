import allure
from locators import Locators
from pages.order_feed_page import OrderFeedPage
from urls import AppUrls


class TestOrderFeed:

    @allure.title("Открытие модального окна заказа")
    @allure.description("Кликаем на первый заказ в ленте, проверяем видимость модального окна с деталями заказа")
    def test_order_feed_open_order_popup(self, browser):
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.open_order_feed_page()
        order_feed_page.click_order_feed_button()
        order_feed_page.click_first_order_in_feed()

        assert order_feed_page.check_element_is_visible(Locators.ORDER_POPUP)

    @allure.title("Отображение заказа пользователя из истории заказов в ленте заказов")
    @allure.description("Делаем заказ, запоминаем его id, форматируем id и находим в общей ленте заказов")
    def test_order_feed_user_order_in_order_feed(self, browser, create_order):
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.click_order_feed_button()
        order_id = create_order
        order_id_in_feed = order_feed_page.find_order_id_in_feed(order_id)
        formatted_order_id = "#0" + order_id

        assert formatted_order_id in order_id_in_feed

    @allure.title("Увеличение счётчика 'за всё время' при новом заказе")
    @allure.description("Запоминаем значение счётчика, делаем заказ, увеличиваем начальное значение на 1")
    def test_order_feed_all_time_counter_increase(self, browser, get_order_counters, create_order):
        all_time_counter, _ = get_order_counters #получаем счётчик до заказа
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.click_order_feed_button()

        assert order_feed_page.get_all_time_counter_int() == all_time_counter + 1

    @allure.title("Увеличение счётчика 'за сегодня' при новом заказе")
    @allure.description("Запоминаем значение счётчика, делаем заказ, увеличиваем начальное значение на 1")
    def test_order_feed_today_counter_increase(self, browser, get_order_counters, create_order):
        _, today_counter = get_order_counters  # получаем счётчик до заказа
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.click_order_feed_button()

        assert order_feed_page.get_today_counter_int() == today_counter + 1

    @allure.title("Отображение заказа в списке 'в работе'")
    def test_order_feed_presence_order_id_in_at_work_list(self, browser, create_order):
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.click_order_feed_button()
        order_id = create_order
        formatted_order_id = "0" + order_id

        assert formatted_order_id == order_feed_page.get_at_work_order_id()
