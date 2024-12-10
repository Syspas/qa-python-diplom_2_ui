import allure

from data.urls import URLS, MainUrl
from helpers.user_data import Person
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage
from pages.login_page import LoginPage


class TestRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Переход на страницу личного кабинета;
                        3. Клик по кнопке "Восстановить пароль";
                        4. Проверка отображения формы восстановления пароля.
                        ''')
    def test_follow_to_the_password_recovery_page(self, driver):
        """
        Проверка перехода на страницу восстановления пароля.
        """
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.move_to_personal_account_btn_and_click()  # Переход в личный кабинет
        login_page.click_recovery_btn()  # Клик по кнопке "Восстановить пароль"
        assert recovery_page.check_recovery_form()  # Проверка формы восстановления пароля
        assert recovery_page.get_current_url() == (MainUrl.MAIN_URL + URLS.url_recovery)  # Проверка правильности URL

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Переход на страницу личного кабинета;
                        3. Клик по кнопке "Восстановить пароль";
                        4. Заполнение поля "Email" корректным значением;
                        5. Клик на кнопку "Восстановить";
                        6. Проверка перехода на страницу сброса пароля.
                        ''')
    def test_input_password_and_click_recovery_btn(self, driver):
        """
        Проверка ввода email и клика по кнопке восстановления пароля.
        """
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.move_to_personal_account_btn_and_click()  # Переход в личный кабинет
        login_page.click_recovery_btn()  # Клик по кнопке "Восстановить пароль"
        recovery_page.send_email_to_email_field(Person.create_data_correct_user()["email"])  # Ввод корректного email
        recovery_page.click_recovery_btn()  # Клик по кнопке "Восстановить"
        assert recovery_page.check_save_btn()  # Проверка наличия кнопки "Сохранить"
        assert recovery_page.get_current_url() == (MainUrl.MAIN_URL + URLS.url_reset_password)  # Проверка правильности URL

    @allure.title('Проверка клика по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Переход на страницу личного кабинета;
                        3. Клик по кнопке "Восстановить пароль";
                        4. Заполнение поля "Email" корректным значением;
                        5. Клик на кнопку "Восстановить";
                        6. Заполнение поля "Пароль";
                        7. Клик на кнопку "Показать";
                        8. Проверка подсветки поля пароля.
                        ''')
    def test_checking_the_backlight_of_the_password_field(self, driver):
        """
        Проверка активации подсветки поля пароля при клике на кнопку "Показать".
        """
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        person_data = Person().create_data_correct_user()
        main_page.move_to_personal_account_btn_and_click()  # Переход в личный кабинет
        login_page.click_recovery_btn()  # Клик по кнопке "Восстановить пароль"
        recovery_page.send_email_to_email_field(person_data.get("email"))  # Ввод email
        recovery_page.click_recovery_btn()  # Клик по кнопке "Восстановить"
        recovery_page.send_password_to_password_field(person_data.get("password"))  # Ввод пароля
        recovery_page.click_show_password_btn()  # Клик по кнопке "Показать"
        assert recovery_page.check_active_password_field(person_data.get("password"))  # Проверка подсветки поля пароля
