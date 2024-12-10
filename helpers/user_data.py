from faker import Faker
import allure


class Person:
    """Метод генерации данных для регистрации"""

    @staticmethod
    @allure.step('Генерация email, password, name пользователя')
    def create_data_correct_user() -> dict:
        """
        Генерирует случайные данные пользователя для регистрации (email, password, name).

        Возвращает:
            dict: Словарь с данными пользователя, включая email, password и name.
        """
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data
