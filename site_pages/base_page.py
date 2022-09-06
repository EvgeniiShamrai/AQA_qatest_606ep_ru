from selenium import webdriver
from selenium.common import NoSuchElementException, NoSuchAttributeException


class BasePage:
    def __init__(self, browser: webdriver.Chrome, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.open_site()

    def open_site(self):
        """Метод перехода на сайт"""
        self.browser.get("https://qatest.606ep.ru/")

    def is_element_on_the_page(self, method, locator):
        """Метод определения наличия html-элемента на странице сайта"""
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def click_element(self, method, locator):
        """Метод нажатия на html-элемент"""
        element = self.browser.find_element(method, locator)
        element.click()

    def get_attr_element(self, method, locator, name_attr):
        """Метод получения атрибута html-элемента"""
        try:
            element = self.browser.find_element(method, locator)
            attr_element = element.get_attribute(name_attr)
        except NoSuchAttributeException:
            return False
        return attr_element
