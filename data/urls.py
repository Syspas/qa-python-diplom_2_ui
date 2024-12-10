class MainUrl:
    """Основной URL для доступа к сайту."""
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'


class URLS:
    """Пути для различных страниц на сайте."""
    url_feed = 'feed'                            # Лента заказов
    url_login = 'login'                          # Страница авторизации
    url_recovery = 'forgot-password'             # Восстановление пароля
    url_register = 'register'                    # Регистрация нового пользователя
    url_profile_area = 'account/profile'         # Личный кабинет
    url_history_order = 'account/order-history'  # История заказов
    url_reset_password = 'reset-password'        # Сброс пароля


class Endpoints:
    """Пути для работы с API."""
    CREATE_USER = 'api/auth/register'   # Создание пользователя
    LOGIN = 'api/auth/login'            # Авторизация
    DELETE_USER = 'api/auth/user'       # Удаление пользователя
    CREATE_ORDER = 'api/orders'         # Создание заказа
    GET_ORDERS = 'api/orders'           # Получение списка заказов
