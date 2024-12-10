import allure

from pages.base_page import BasePage
from locators.locators import MainPageLocators
from locators.locators import HeaderPageLocatrors


class HeaderPage(BasePage):
    """Методы взаимодействия с хедером"""

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_btn(self):
        """
        Кликает по кнопке 'Конструктор' на хедере страницы.
        """
        self.move_to_element_and_click(HeaderPageLocatrors.constructor_btn)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_feed_btn(self):
        """
        Кликает по кнопке 'Лента заказов' на хедере страницы.
        """
        self.move_to_element_and_click(HeaderPageLocatrors.order_feed_btn)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_profile_area_btn(self):
        """
        Кликает по кнопке 'Личный кабинет' на хедере страницы.
        """
        self.move_to_element_and_click(HeaderPageLocatrors.personal_account_btn)


class MainPage(BasePage):
    """Методы взаимодействия с главной страницей"""

    @allure.step('Переход к кнопке "Личный Кабинет" и клик на нее')
    def move_to_personal_account_btn_and_click(self):
        """
        Переходит к кнопке 'Личный кабинет' и кликает по ней на главной странице.
        """
        self.move_to_element_and_click(MainPageLocators.personal_account_btn)

    @allure.step('Проверка отображения формы конструктор')
    def check_constructor_form(self):
        """
        Проверяет отображение формы конструктора на главной странице.

        :return: элемент формы конструктора
        """
        return self.check_element(MainPageLocators.constructor_form)

    @allure.step('Проверка отображения формы ленты заказов')
    def check_orders_feed_form(self):
        """
        Проверяет отображение формы ленты заказов на главной странице.

        :return: элемент формы ленты заказов
        """
        return self.check_element(MainPageLocators.order_feed_form)

    @allure.step('Клик по Флюорисцентной булке RD-D3')
    def click_fluorescent_bun_btn(self):
        """
        Кликает по кнопке флюорисцентной булки на главной странице.
        """
        self.click_button(MainPageLocators.fluorescent_bun_btn)

    @allure.step('Проверка отображения формы "Информации о булке"')
    def check_fluorescent_bun_form(self):
        """
        Проверяет отображение формы информации о флюорисцентной булке.

        :return: элемент формы информации о булке
        """
        return self.check_element(MainPageLocators.popup_form_ingrediens)

    @allure.step('Проверка закрытия формы "Информация о булке"')
    def check_close_fluorescent_bun_form(self):
        """
        Проверяет, что форма информации о флюорисцентной булке закрыта.

        :return: элемент, который не виден на странице
        """
        return self.check_element_is_not_visible(MainPageLocators.popup_form_ingrediens)

    @allure.step('Закрытие формы информации об ингридиенте')
    def close_popup_form(self):
        """
        Закрывает форму информации о булке.
        """
        self.move_to_element_and_click(MainPageLocators.close_popup_form)

    @allure.step('Добавить булку в корзину')
    def add_bun(self):
        """
        Перетаскивает флюорисцентную булку в корзину.
        """
        self.drag_and_drop(MainPageLocators.fluorescent_bun_btn, MainPageLocators.order_basket)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_place_order_button(self):
        """
        Кликает по кнопке 'Оформить заказ' на главной странице.
        """
        self.click_button(MainPageLocators.place_order_button)

    @allure.step('Создание заказа')
    def create_order(self):
        """
        Создает заказ, добавляя булку в корзину и кликая по кнопке 'Оформить заказ'.
        """
        self.add_bun()
        self.click_place_order_button()

    @allure.step('Получение значения счетчика ингредиента')
    def check_counter_ingredient(self):
        """
        Получает значение счетчика ингредиента (сколько булок добавлено в корзину).

        :return: текст счетчика ингредиента
        """
        return self.get_text_locator(MainPageLocators.counter_ingredient)

    @allure.step('Проверка отображения формы Оформление заказа')
    def check_order_form(self):
        """
        Проверяет отображение формы оформления заказа на главной странице.

        :return: элемент формы оформления заказа
        """
        return self.check_element(MainPageLocators.order_form)

    @allure.step('Получение номера оформленного заказа')
    def get_order_number(self):
        """
        Получает номер оформленного заказа на главной странице.

        :return: номер заказа
        """
        return self.get_text_locator(MainPageLocators.order_num)

    @allure.step('Ожидание загрузки кнопки Оформить заказ')
    def wait_load_main_page(self):
        """
        Ожидает загрузку кнопки 'Оформить заказ' на главной странице.
        """
        self.wait_for_load_element(MainPageLocators.place_order_button)
