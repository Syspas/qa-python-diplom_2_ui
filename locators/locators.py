from selenium.webdriver.common.by import By


class HeaderPageLocators:
    """Локаторы для элементов в хедере (верхняя часть страницы)."""

    constructor_btn = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")                            # Кнопка "Конструктор"
    order_feed_btn = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")                           # Кнопка "Лента заказов"
    personal_account_btn = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")                    # Кнопка "Личный кабинет"


class MainPageLocators:
    """Локаторы для элементов на главной странице."""

    order_feed_form = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")                    # Форма ленты заказов
    constructor_form = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']") # Форма конструктора
    place_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")                          # Кнопка "Оформить заказ"
    fluorescent_bun_btn = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")                  # Кнопка флюоресцентной булки
    close_popup_form = (By.XPATH, '//button[contains(@class,"close")]')                              # Кнопка закрытия модального окна
    counter_ingredient = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")         # Счетчик ингредиента
    order_form = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")                      # Форма оформленного заказа
    order_basket = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")             # Корзина
    order_num = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")            # Номер заказа
    personal_account_btn = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")              # Кнопка "Войти в аккаунт"
    popup_form_ingrediens = (By.XPATH, "//h2[text()= 'Детали ингредиента']")                         # Модальное окно "Детали ингредиента"


class AuthPageLocators:
    """Локаторы для элементов на странице авторизации."""

    auth_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")                                   # Форма авторизации
    email_input = (By.XPATH, ".//input[@name = 'name']")                                             # Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")                                        # Поле ввода пароля
    login_account_btn = (By.XPATH, "//button[text() = 'Войти']")                                     # Кнопка "Войти"
    registration_btn = (By.XPATH, "//a[text() = 'Зарегистрироваться']")                              # Кнопка "Зарегистрироваться"
    recover_btn = (By.XPATH, "//a[text() = 'Восстановить пароль']")                                  # Кнопка "Восстановить пароль"


class RecoveryPageLocators:
    """Локаторы для элементов на странице восстановления пароля."""

    email_input = (By.XPATH, ".//input[@name = 'name']")                                             # Поле ввода email
    recover_btn = (By.XPATH, ".//button[text() = 'Восстановить']")                                   # Кнопка "Восстановить"
    login_account_btn = (By.XPATH, ".//a[text() = 'Войти']")                                         # Кнопка "Войти"
    password_input = (By.XPATH, ".//input[@name = 'Введите новый пароль']")                          # Поле ввода нового пароля
    code_from_mail = (By.XPATH, ".//label[text() = 'Введите код из письма']")                        # Поле ввода кода из письма
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']")                                         # Кнопка "Сохранить"
    recovery_text_form = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")                       # Заголовок формы восстановления пароля
    show_btn = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")                       # Кнопка "Показать пароль"
    input_field_active = (By.CSS_SELECTOR, ".input.input_status_active")                             # Подсветка активного поля ввода пароля


class PersonalAreaLocators:
    """Локаторы для элементов на странице личного кабинета."""

    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")                           # Форма личного кабинета
    profile_btn = (By.XPATH, ".//a[text() = 'Профиль']")                                             # Кнопка "Профиль"
    order_history_btn = (By.XPATH, ".//a[text() = 'История заказов']")                               # Кнопка "История заказов"
    history_order_form = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")                  # Форма истории заказов
    number_order = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")                  # Номер заказа
    cancel_btn = (By.XPATH, ".//button[text() = 'Отмена']")                                          # Кнопка "Отмена"
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']")                                         # Кнопка "Сохранить"
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']")                                             # Кнопка "Выход"


class OrderFeedLocators:
    """Локаторы для элементов на странице ленты заказов."""

    title_orders_list = (By.XPATH, '//h1[text()="Лента заказов"]')                                   # Заголовок страницы "Лента заказов"
    orders_info = (By.XPATH, '//p[text()="Cостав"]')                                                 # Детали заказа
    total_orders_counter = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")  # Счетчик заказов за все время
    dayly_orders_counter = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")    # Счетчик заказов за сегодня
    number_order_in_job = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")          # Заказы "В работе"
    order_info_window = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")     # Первый заказ в истории
    order_history = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')                 # Все заказы в ленте
