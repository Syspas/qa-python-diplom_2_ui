import allure

from pages.base_page import BasePage
from locators.locators import RecoveryPageLocators


class RecoveryPage(BasePage):
    """Методы взаимодействия со страницей 'Восстановление пароля'"""

    @allure.step('Проверка формы восстановления пароля')
    def check_recovery_form(self):
        """
        Проверяет отображение формы для восстановления пароля.

        :return: элемент формы восстановления пароля
        """
        return self.check_element(RecoveryPageLocators.recovery_text_form)

    @allure.step('Заполнение формы Email')
    def send_email_to_email_field(self, email):
        """
        Заполняет поле для ввода Email.

        :param email: Email для ввода в поле
        """
        self.send_keys_to_field(RecoveryPageLocators.email_input, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_recovery_btn(self):
        """
        Кликает по кнопке для начала восстановления пароля.
        """
        self.click_button(RecoveryPageLocators.recover_btn)

    @allure.step('Клик по кнопке "Войти"')
    def click_login_btn(self):
        """
        Кликает по кнопке для перехода на страницу авторизации.
        """
        self.click_button(RecoveryPageLocators.login_account_btn)

    @allure.step('Заполнение поля Пароль')
    def send_password_to_password_field(self, password):
        """
        Заполняет поле для ввода нового пароля.

        :param password: новый пароль
        """
        self.send_keys_to_field(RecoveryPageLocators.password_input, password)

    @allure.step('Заполнение поля "Код из письма"')
    def send_code_to_code_field(self, code):
        """
        Заполняет поле для ввода кода, полученного на email.

        :param code: код для ввода в поле
        """
        self.send_keys_to_field(RecoveryPageLocators.code_from_mail, code)

    @allure.step('Клик по кнопке "Сохранить"')
    def click_save_btn(self):
        """
        Кликает по кнопке для сохранения нового пароля.
        """
        self.click_button(RecoveryPageLocators.save_btn)

    @allure.step('Проверка подсветки поля "Пароль"')
    def check_active_password_field(self, password):
        """
        Проверяет, что поле для ввода пароля активно и отображается.

        :param password: новый пароль для проверки
        :return: элемент поля пароля, если оно активно
        """
        self.send_password_to_password_field(password)
        self.click_button(RecoveryPageLocators.show_btn)
        return self.check_element(RecoveryPageLocators.input_field_active)

    @allure.step('Проверка отображения кнопки "Сохранить"')
    def check_save_btn(self):
        """
        Проверяет, что кнопка "Сохранить" отображается на странице.

        :return: элемент кнопки "Сохранить"
        """
        return self.check_element(RecoveryPageLocators.save_btn)
