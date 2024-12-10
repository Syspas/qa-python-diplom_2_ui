import allure

from pages.base_page import BasePage
from locators.locators import AuthPageLocators


class LoginPage(BasePage):
    """Методы взаимодействия с формой авторизации"""

    @allure.step('Проверка отображения формы логина')
    def check_authorization_form_verification(self):
        """
        Проверяет отображение формы авторизации на странице.

        :return: элемент формы авторизации
        """
        return self.check_element(AuthPageLocators.auth_form)

    @allure.step('Заполнение поля "Email"')
    def send_email_to_email_field(self, email):
        """
        Заполняет поле 'Email' на странице авторизации.

        :param email: email пользователя
        """
        self.send_keys_to_field(AuthPageLocators.email_input, email)

    @allure.step('Заполнение поля "Password"')
    def send_password_to_password_field(self, password):
        """
        Заполняет поле 'Пароль' на странице авторизации.

        :param password: пароль пользователя
        """
        self.send_keys_to_field(AuthPageLocators.password_input, password)

    @allure.step('Клик на кнопку "Войти"')
    def click_login_btn(self):
        """
        Кликает по кнопке 'Войти' на странице авторизации.
        """
        self.move_to_element_and_click(AuthPageLocators.login_account_btn)

    @allure.step('Авторизация на сайте')
    def login(self, email, password):
        """
        Выполняет авторизацию на сайте, заполняя поля 'Email' и 'Пароль',
        затем кликая по кнопке 'Войти'.

        :param email: email пользователя
        :param password: пароль пользователя
        """
        self.send_email_to_email_field(email)
        self.send_password_to_password_field(password)
        self.click_login_btn()

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_recovery_btn(self):
        """
        Кликает по кнопке 'Восстановить пароль' на странице авторизации.
        """
        self.move_to_element_and_click(AuthPageLocators.recover_btn)

    @allure.step('Клик на кнопку "Зарегистрироваться"')
    def click_register_btn(self):
        """
        Кликает по кнопке 'Зарегистрироваться' на странице авторизации.
        """
        self.move_to_element_and_click(AuthPageLocators.registration_btn)
