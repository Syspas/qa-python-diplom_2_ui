import allure

from data.urls import URLS, MainUrl
from pages.main_page import MainPage, HeaderPage


class TestMainPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Клик по кнопке "Войти в аккаунт";
                        3. Клик по кнопке "Конструктор";
                        4. Проверяем отображение формы "Конструктор".
                        ''')
    def test_follow_to_constructor_page(self, driver):
        """
        Проверка перехода на страницу конструктора через хедер.
        """
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        main_page.move_to_personal_account_btn_and_click()  # Переход в личный кабинет
        header.click_constructor_btn()  # Клик по кнопке "Конструктор"
        assert main_page.check_constructor_form() and main_page.get_current_url() == MainUrl.MAIN_URL

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Клик по кнопке "Лента заказов";
                        3. Проверяем отображение формы "Лента заказов".
                        ''')
    def test_follow_to_orders_feed_page(self, driver):
        """
        Проверка перехода на страницу ленты заказов.
        """
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_feed_btn()  # Клик по кнопке "Лента заказов"
        assert main_page.check_orders_feed_form() and main_page.get_current_url() == (MainUrl.MAIN_URL + URLS.url_feed)

    @allure.title('Проверка если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Клик по кнопке "Флюорисцентная булка R2-D3";
                        3. Проверка отображения всплывающего окна с деталями ингредиента.
                        ''')
    def test_check_fluorescent_bun_form(self, driver):
        """
        Проверка открытия формы с информацией о булке при клике на ингредиент.
        """
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_btn()  # Клик по булке
        assert main_page.check_fluorescent_bun_form()  # Проверка наличия формы с деталями

    @allure.title('Проверка закрытия всплывающего окна по крестику')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Клик по кнопке "Флюорисцентная булка R2-D3";
                        3. Клик по крестику модального окна;
                        4. Проверка закрытия формы "Информация об ингредиенте".
                        ''')
    def test_close_fluorescent_bun_form(self, driver):
        """
        Проверка закрытия формы с информацией о булке.
        """
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_btn()  # Открытие формы
        main_page.close_popup_form()  # Закрытие формы
        assert main_page.check_close_fluorescent_bun_form()  # Проверка, что форма закрыта

    @allure.title('Проверка при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Добавление "Флюорисцентной булки R2-D3 в корзину";
                        3. Проверка увеличения счетчика ингредиента.
                        ''')
    def test_counter_ingredient(self, driver):
        """
        Проверка увеличения счетчика ингредиентов в корзине.
        """
        main_page = MainPage(driver)
        main_page.add_bun()  # Добавление булки в корзину
        assert int(main_page.check_counter_ingredient()) > 0  # Проверка увеличения счетчика

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переход на страницу сервиса;
                        3. Логин в системе;
                        4. Добавление "Флюорисцентной булки R2-D3 в корзину";
                        5. Клик по кнопке "Оформить заказ";
                        6. Проверка отображения формы заказа;
                        7. Удаляем пользователя через API.
                        ''')
    def test_create_order(self, driver, create_new_user, login):
        """
        Проверка возможности оформления заказа пользователем.
        """
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_constructor_btn()  # Переход к конструктору
        main_page.create_order()  # Создание заказа
        assert main_page.check_order_form()  # Проверка отображения формы оформления заказа

