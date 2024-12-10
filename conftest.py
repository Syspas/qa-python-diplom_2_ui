import pytest
from selenium import webdriver
import requests

from data.urls import MainUrl
from helpers.user_data import Person
from data.urls import Endpoints
from data.ingredients import Ingredients
from pages.main_page import HeaderPage, MainPage
from pages.login_page import LoginPage

# Фикстура для создания веб-драйвера, запускающего тесты на разных браузерах (Chrome, Firefox)
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    """
    Фикстура для инициализации веб-драйвера на основе выбранного браузера.
    """
    if request.param == 'chrome':
        driver = webdriver.Chrome()  # Инициализация Chrome WebDriver
        driver.set_window_size(1920, 1080)  # Установка размера окна браузера
        driver.get(MainUrl.MAIN_URL)  # Переход на главную страницу
    elif request.param == 'firefox':
        driver = webdriver.Firefox()  # Инициализация Firefox WebDriver
        driver.set_window_size(1920, 1080)  # Установка размера окна браузера
        driver.get(MainUrl.MAIN_URL)  # Переход на главную страницу
    yield driver  # Передача драйвера для использования в тестах
    driver.quit()  # Завершаем сессию драйвера после выполнения теста


# Фикстура для создания нового пользователя через API
@pytest.fixture
def create_new_user():
    """
    Фикстура для создания нового пользователя через API и удаления его после теста.
    """
    payload = Person.create_data_correct_user()  # Получение данных для создания пользователя
    response = requests.post(MainUrl.MAIN_URL + Endpoints.CREATE_USER, data=payload)  # Запрос на создание пользователя через API
    yield payload, response  # Возвращаем данные пользователя и ответ от сервера
    token = response.json()["accessToken"]  # Получение токена для аутентификации
    requests.delete(MainUrl.MAIN_URL + Endpoints.DELETE_USER, headers={"Authorization": token})  # Удаление пользователя после теста


# Фикстура для логина пользователя
@pytest.fixture
def login(driver, create_new_user):
    """
    Фикстура для логина в систему с помощью данных созданного пользователя.
    """
    create_user_data = create_new_user[0]  # Получение данных созданного пользователя
    header_page = HeaderPage(driver)  # Инициализация страницы с заголовком
    login_page = LoginPage(driver)  # Инициализация страницы логина
    header_page.click_profile_area_btn()  # Клик по кнопке "Личный кабинет"
    login_page.login(create_user_data["email"], create_user_data["password"])  # Ввод данных для логина
    main_page = MainPage(driver)  # Инициализация главной страницы
    main_page.wait_load_main_page()  # Ожидание загрузки главной страницы после логина


# Фикстура для создания заказа через API
@pytest.fixture
def create_order(create_new_user):
    """
    Фикстура для создания нового заказа через API и возврата его номера.
    """
    token = create_new_user[1].json()["accessToken"]  # Получение токена пользователя
    headers = {'Authorization': token}  # Заголовок с токеном для аутентификации
    response = requests.post(MainUrl.MAIN_URL + Endpoints.CREATE_ORDER, headers=headers, data=Ingredients.correct_ingredients_data)  # Создание заказа через API
    return response.json()["order"]["number"]  # Возвращаем номер созданного заказа


# Для корректного отображения аргументов в параметризированном тесте
def pytest_make_parametrize_id(val):
    """
    Функция для корректного отображения аргументов в параметризированном тесте.
    """
    return repr(val)  # Возвращаем строковое представление значения
