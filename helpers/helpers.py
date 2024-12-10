from data.ingredients import Ingredients
from data.urls import MainUrl, Endpoints
import requests
import allure


class Order:
    """Методы отправки запросов API для создания и получения номеров заказов."""

    @allure.step('Создание нового заказа пользователя через API')
    def create_order(self, create_new_user):
        """
        Создает новый заказ для пользователя через API.

        Аргументы:
            create_new_user (tuple): Кортеж с данными о новом пользователе, где
                                      [1] - ответ от API с токеном доступа.

        Возвращает:
            None: Просто отправляет запрос на создание заказа.
        """
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}

        # Отправка POST запроса для создания нового заказа с данными ингредиентов
        response = requests.post(MainUrl.MAIN_URL + Endpoints.CREATE_ORDER, headers=headers, data=Ingredients.correct_ingredients_data)

        # Можно добавить обработку ошибок, чтобы удостовериться, что заказ был успешно создан
        if response.status_code != 201:
            raise Exception(f"Не удалось создать заказ. Статус: {response.status_code}, Ответ: {response.text}")

    @allure.step('Получение заказов пользователя через API')
    def get_user_orders(self, create_new_user):
        """
        Получает список заказов пользователя через API и возвращает номер первого заказа.

        Аргументы:
            create_new_user (tuple): Кортеж с данными о новом пользователе, где
                                      [1] - ответ от API с токеном доступа.

        Возвращает:
            str: Номер первого заказа пользователя.
        """
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}

        # Отправка GET запроса для получения списка заказов
        response = requests.get(MainUrl.MAIN_URL + Endpoints.GET_ORDERS, headers=headers)

        # Проверка на успешный ответ и наличие заказов
        if response.status_code != 200:
            raise Exception(f"Не удалось получить заказы. Статус: {response.status_code}, Ответ: {response.text}")

        orders = response.json().get("orders", [])
        if not orders:
            raise Exception("У пользователя нет заказов.")

        # Возвращаем номер первого заказа
        return orders[0]["number"]
