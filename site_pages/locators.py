from selenium.webdriver.common.by import By


# Набор локаторов для поиска html-элементов
class FirstPageLocators:
    USER_AGREEMENT = (By.CSS_SELECTOR, ".Home_agreed__8Ycv8")
    LINK_USER_AGREEMENT = (By.CSS_SELECTOR, ".Home_agreed__8Ycv8  > a")
    LOGIN_FIELD = (By.CSS_SELECTOR, ".Home_content__Zy02X>div:nth-child(2) > input")
    PASSWORD_FIELD = (By.CSS_SELECTOR, ".Home_content__Zy02X>div:nth-child(3) > input")
    BUTTON_ENTER_LOGIN_FORM = (By.CSS_SELECTOR, ".Home_button__Zs7A2")
    REQUIRED_LOGIN_FIELD = (By.CSS_SELECTOR, 'Home_content__Zy02X>div:nth-child(2) > input[required]')
    REQUIRED_PASSWORD_FIELD = (By.CSS_SELECTOR, 'Home_content__Zy02X>div:nth-child(3) > input[required]')
