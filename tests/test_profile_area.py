import allure

from data.urls import URLS, MainUrl
from pages.main_page import HeaderPage
from pages.login_page import LoginPage
from pages.profile_area_page import ProfileAreaPage


class TestProfileAreaPage:

    @allure.title('Проверка перехода в "Личный кабинет"')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переход на страницу сервиса;
                        3. Логин в систему;
                        4. Клик по кнопке "Личный кабинет";
                        5. Проверка отображения формы "Личный кабинет";
                        6. Проверка правильности текущего URL;
                        7. Удаляем пользователя через API.
                        ''')
    def test_follow_to_profile_area_page(self, driver, create_new_user, login):
        """
        Проверка перехода в "Личный кабинет" через кнопку.
        """
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        header.click_profile_area_btn()  # Переход в "Личный кабинет"
        assert profile_area.check_profile_area_form()  # Проверка формы "Личный кабинет"
        assert profile_area.get_current_url() == (MainUrl.MAIN_URL + URLS.url_profile_area)  # Проверка правильности URL

    @allure.title('Проверка перехода в "История Заказов"')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переход на страницу сервиса;
                        3. Логин в систему;
                        4. Клик по кнопке "Личный кабинет";
                        5. Клик по кнопке "История заказов";
                        6. Проверка отображения формы "История заказов";
                        7. Проверка правильности текущего URL;
                        8. Удаляем пользователя через API.
                        ''')
    def test_follow_to_feed_orders(self, driver, create_new_user, login):
        """
        Проверка перехода в раздел "История заказов" через кнопку.
        """
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        header.click_profile_area_btn()  # Переход в "Личный кабинет"
        profile_area.click_history_orders_btn()  # Клик по кнопке "История заказов"
        assert profile_area.check_profile_area_form()  # Проверка формы "История заказов"
        assert profile_area.get_current_url() == (MainUrl.MAIN_URL + URLS.url_history_order)  # Проверка правильности URL

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переход на страницу сервиса;
                        3. Логин в систему;
                        4. Клик по кнопке "Личный кабинет";
                        5. Клик по кнопке "Выход";
                        6. Проверка выхода из аккаунта (возвращение на страницу логина);
                        7. Удаляем пользователя через API.
                        ''')
    def test_exit_profile_area(self, driver, create_new_user, login):
        """
        Проверка выхода из аккаунта.
        """
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        login_page = LoginPage(driver)
        header.click_profile_area_btn()  # Переход в "Личный кабинет"
        profile_area.click_exit_btn()  # Клик по кнопке "Выход"
        assert login_page.check_authorization_form_verification()  # Проверка возвращения на страницу логина
        assert login_page.get_current_url() == (MainUrl.MAIN_URL + URLS.url_login)  # Проверка правильности URL
