import allure

from locators.locators import PersonalAreaLocators
from pages.base_page import BasePage


class ProfileAreaPage(BasePage):
    """Методы взаимодействия со страницей 'Личный кабинет'"""

    @allure.step('Проверка отображения формы "Личного кабинета"')
    def check_profile_area_form(self):
        """
        Проверяет отображение формы 'Личный кабинет'.

        :return: элемент формы 'Личный кабинет'
        """
        return self.check_element(PersonalAreaLocators.profile_form)

    @allure.step('Клик по кнопке "Профиль"')
    def click_profile_btn(self):
        """
        Кликает по кнопке 'Профиль' на странице личного кабинета.
        """
        self.click_button(PersonalAreaLocators.profile_btn)

    @allure.step('Клик по кнопке "История заказов"')
    def click_history_orders_btn(self):
        """
        Кликает по кнопке 'История заказов' на странице личного кабинета.
        """
        self.click_button(PersonalAreaLocators.order_history_btn)

    @allure.step('Проверка отображения формы "История заказов"')
    def check_history_form(self):
        """
        Проверяет отображение формы 'История заказов' на странице личного кабинета.

        :return: элемент формы 'История заказов'
        """
        return self.check_element(PersonalAreaLocators.history_order_form)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_btn(self):
        """
        Кликает по кнопке 'Выход' для выхода из личного кабинета.
        """
        self.click_button(PersonalAreaLocators.exit_btn)

    @allure.step('Клик по кнопке "Отмена"')
    def click_cansel_btn(self):
        """
        Кликает по кнопке 'Отмена' для отмены действия (например, выхода).
        """
        self.click_button(PersonalAreaLocators.exit_btn)

    @allure.step('Клик по кнопке "Сохранить"')
    def click_save_btn(self):
        """
        Кликает по кнопке 'Сохранить' для сохранения изменений на странице личного кабинета.
        """
        self.click_button(PersonalAreaLocators.save_btn)

    @allure.step('Получение номера заказа в истории')
    def get_orders_number(self):
        """
        Получает номер заказа из истории заказов.

        :return: номер заказа
        """
        return self.get_text_locator(PersonalAreaLocators.number_order)
