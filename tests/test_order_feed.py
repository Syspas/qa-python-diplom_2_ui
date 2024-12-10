import allure
import pytest

from pages.main_page import HeaderPage
from pages.order_feed_page import OrderFeedPage
from locators.locators import OrderFeedLocators
from helpers.helpers import Order


class TestOrderFeedPage:

    @allure.title('Проверка, что при клике на заказ откроется всплывающее окно с деталями')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Клик по кнопке "Лента заказов";
                        3. Клик на первый заказ;
                        4. Проверка отображения формы с деталями заказа.
                        ''')
    def test_check_order_info_window(self, driver):
        """
        Проверка отображения всплывающего окна с деталями заказа при клике на заказ.
        """
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()  # Переход в "Лента заказов"
        feed_order.click_order_info()  # Клик по первому заказу
        assert feed_order.check_order_info_window()  # Проверка отображения формы с деталями

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе "В работе"')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переход на страницу сервиса;
                        3. Логин в систему;
                        4. Переход на страницу "Лента заказов";
                        5. Получаем заказ в списке "В работе";
                        6. Получаем список заказов пользователя;
                        7. Проверяем, что заказ пользователя в списке заказов "В работе";
                        8. Удаляем пользователя через API.
                        ''')
    def test_check_user_order_in_job(self, driver, create_new_user, login):
        """
        Проверка, что заказ появляется в разделе "В работе" после его оформления.
        """
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()  # Переход в "Лента заказов"
        order.create_order(create_new_user)  # Создание нового заказа через API
        orders_in_jobs = feed_order.get_orders_in_jobs()  # Получение списка заказов в "В работе"
        user_order = str(order.get_user_orders(create_new_user))  # Получение заказа пользователя
        assert user_order in orders_in_jobs  # Проверка наличия заказа в списке "В работе"

    @allure.title('Проверка, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Создаем заказ через API;
                        3. Переходим на страницу сервиса;
                        4. Логин в систему;
                        5. Переход на страницу "Лента заказов";
                        6. Получаем заказ пользователя через API;
                        7. Получаем список заказов на странице "Лента заказов";
                        8. Проверяем отображение заказа пользователя;
                        9. Удаляем пользователя через API.
                        ''')
    def test_check_user_orders_in_orders_history(self, driver, create_new_user, create_order, login):
        """
        Проверка отображения заказов пользователя из раздела "История заказов" на странице "Лента заказов".
        """
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()  # Переход в "Лента заказов"
        user_order = str(order.get_user_orders(create_new_user))  # Получение заказа пользователя
        orders_history_in_feed = feed_order.get_orders_history()  # Получение истории заказов на странице "Лента заказов"
        assert user_order in orders_history_in_feed  # Проверка отображения заказа в "Лента заказов"

    @allure.title('Проверка, что при создании нового заказа счетчик «Выполнено за всё время» / «Выполнено за сегодня» увеличивается')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переходим на страницу сервиса;
                        3. Логин в систему;
                        4. Переход на страницу "Лента заказов";
                        5. Получаем текущее значение счетчика;
                        6. Отправляем запрос на создание заказа через API;
                        7. Проверяем увеличение счетчика;
                        8. Удаляем пользователя через API.
                        ''')
    @pytest.mark.parametrize('counter', [OrderFeedLocators.dayly_orders_counter, OrderFeedLocators.total_orders_counter])
    def test_update_counter_orders(self, driver, create_new_user, login, counter):
        """
        Проверка увеличения счетчиков выполненных заказов.
        """
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()  # Переход в "Лента заказов"
        now_counter = int(feed_order.check_counter_orders(counter))  # Текущее значение счетчика
        order.create_order(create_new_user)  # Создание нового заказа через API
        new_counter = int(feed_order.check_counter_orders(counter))  # Новое значение счетчика
        assert new_counter > now_counter  # Проверка увеличения счетчика
