from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import allure
from data.urls import BASE_URL

class Base_page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Поиск нескольких элементов по локатору")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    @allure.step("Добавление текста")
    def add_text_element(self, locator, keys):
        self.find_element(locator).send_keys(keys)

    @allure.step("Получение текста из элемента")
    def get_text_element(self, locator):
        return self.find_element(locator).text

    @allure.step("Видимость элемента")
    def visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Получение урла")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Проверка перехода на страницу")
    def wait_for_redirect(self, text):
        self.wait.until(EC.url_contains(text))

    @allure.step("Проверка видимости элемента с ожиданием")
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Проверка не видимости элемента с ожиданием")
    def wait_for_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element(locator))

    @allure.step("Проверка видимости элемента")
    def is_visible_element(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Скролл к элементу")
    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def move_to_element(self, locator):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()


    def renew(self, locator):
        element = self.find_element(locator)
        element.renew()


    @allure.step("Перетаскивание элемента на странице")
    def drag_and_drop_element(self, source_element, target_element):
        script = """
                function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                    var dataTransfer = new DataTransfer();
                    var dragStartEvent = new DragEvent('dragstart', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragStartEvent);

                    var dropEvent = new DragEvent('drop', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    destinationNode.dispatchEvent(dropEvent);
                    var dragEndEvent = new DragEvent('dragend', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragEndEvent);
                }
                simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                """
        self.driver.execute_script(script, source_element, target_element)

    @allure.step("Кликнуть на элемент в Firefox")
    def click_on_element(self, locator):
        target = self.wait_for_visible(locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    def forse_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)