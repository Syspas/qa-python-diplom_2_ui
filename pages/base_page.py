from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    """Базовый класс для взаимодействия с элементами страницы."""

    def __init__(self, driver):
        """
        Инициализация класса с драйвером.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver

    # Получить текущий URL страницы
    def get_current_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url

    # Ожидание кликабельности элемента
    def wait_element_clickable(self, locator):
        """
        Ожидает, пока элемент не станет кликабельным.

        :param locator: локатор элемента
        """
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    # Ожидание загрузки элемента на странице
    def wait_for_load_element(self, locator):
        """
        Ожидает, пока элемент не станет видимым на странице.

        :param locator: локатор элемента
        """
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))

    # Клик по кнопке
    def click_button(self, locator):
        """
        Выполняет клик по элементу.

        :param locator: локатор элемента
        """
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).click()

    # Заполнение поля формы
    def send_keys_to_field(self, locator, text):
        """
        Вводит текст в поле.

        :param locator: локатор поля
        :param text: текст для ввода
        """
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)

    # Получить текст из элемента
    def get_text_locator(self, locator):
        """
        Возвращает текст элемента.

        :param locator: локатор элемента
        :return: текст элемента
        """
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    # Получить текст из нескольких элементов
    def get_text_locators(self, locator):
        """
        Возвращает тексты из всех найденных элементов.

        :param locator: локатор элементов
        :return: список текстов элементов
        """
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    # Проверка наличия элемента на странице
    def check_element(self, locator):
        """
        Проверяет наличие элемента на странице.

        :param locator: локатор элемента
        :return: элемент, если он найден
        """
        self.wait_for_load_element(locator)
        return self.driver.find_element(*locator)

    # Проверка, что элемент не виден на странице
    def check_element_is_not_visible(self, locator):
        """
        Проверяет, что элемент стал невидимым.

        :param locator: локатор элемента
        :return: элемент, если он невидим
        """
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Перетаскивание элемента
    def drag_and_drop(self, element_one, element_two):
        """
        Выполняет перетаскивание одного элемента на другой.

        :param element_one: локатор элемента, который нужно перетащить
        :param element_two: локатор элемента, на который нужно перетащить
        """
        element = self.driver.find_element(*element_one)
        target = self.driver.find_element(*element_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    # Переход к элементу и клик по нему
    def move_to_element_and_click(self, locator):
        """
        Перемещает курсор к элементу и кликает по нему.

        :param locator: локатор элемента
        """
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
