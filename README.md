# Дипломный проект. Задание 3: UI - Автотесты для сервиса **"Stellar Burger"**

Сайт: `https://stellarburgers.nomoreparties.site/`

#### **Описание структуры проекта:**

1. **Каталог отчетов:**
    - `allure_results` — каталог для хранения отчетов о тестировании, генерируемых Allure.

2. **Тестовые файлы:**
    - `tests/test_main_page.py` — содержит тесты основного функционала сервиса.
    - `tests/test_order_feed.py` — включает тесты для проверки работы ленты заказов.
    - `tests/test_profile_area.py` — тестирует функции личного кабинета.
    - `tests/test_recovery_page.py` — проверяет функционал восстановления пароля.

3. **Файлы с локаторами:**
    - `locators/locators.py` — файл, содержащий локаторы элементов интерфейса для работы с ними в тестах.

4. **Файлы вспомогательных функций:**
    - `helpers/user_data.py` — генерация данных для регистрации пользователей.
    - `helpers/helpers.py` — методы создания и получения заказов через API.

5. **Файлы с данными:**
    - `data/urls` — список URL сервиса и его ручек API.
    - `data/ingredients.py` — данные об ингредиентах для сборки заказа.

6. **Файлы взаимодействия с UI:**
    - `pages/base_page.py` — базовые методы взаимодействия с элементами интерфейса.
    - `pages/login_page.py` — методы для работы со страницей логина.
    - `pages/main_page.py` — методы работы с главной страницей.
    - `pages/order_feed_page.py` — взаимодействие с лентой заказов.
    - `pages/profile_area_page.py` — функционал личного кабинета.
    - `pages/recovery_page.py` — работа со страницей восстановления пароля.

7. **Конфигурационные файлы:**
    - `requirements.txt` — содержит список внешних зависимостей.
    - `conftest.py` — файл для фикстур Pytest, необходимых для выполнения тестов.

---

#### **Инструкции для работы с проектом:**