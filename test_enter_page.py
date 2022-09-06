import pytest

from site_pages import EnterPage
from site_pages import FirstPageLocators


@pytest.mark.xfail(reason='Add a user agreement link')
def test_should_be_go_to_link_user_agreement(browser):
    """Тест-кейс №1  проверка перехода по ссылке 'Пользовательского соглашения'"""
    ep = EnterPage(browser)
    ep.should_be_click_on_the_link_user_agreement()


@pytest.mark.xfail(reason='Change the attributes in the Login and Password fields')
def test_checking_display_entered_data_in_login_password_fields(browser):
    """Тест-кейс №2 проверка отбоажения данных в полях 'Логин' и 'Пароль'"""
    ep = EnterPage(browser)
    browser.find_element(*FirstPageLocators.LOGIN_FIELD).send_keys('My-Live')
    browser.find_element(*FirstPageLocators.PASSWORD_FIELD).send_keys('HowMathIsTheFish123')
    ep.checking_display_entered_data_in_login_fields()
    ep.checking_display_entered_data_in_password_fields()


#
@pytest.mark.xfail(reason="This is a blocking bug to fix first")
def test_should_be_go_to_greeting_form(browser):
    """Тест-кейс №3 проверка перехода на форму 'Преветствие'"""
    ep = EnterPage(browser)
    browser.find_element(*FirstPageLocators.LOGIN_FIELD).send_keys('My-Live')
    browser.find_element(*FirstPageLocators.PASSWORD_FIELD).send_keys('HowMathIsTheFish123')
    ep.should_be_click_on_the_button_enter_the_login_form()


@pytest.mark.xfail(reason="The 'Login' field must be filled in")
def test_login_field_should_be_mandatory(browser):
    """Тесе-кейс №4 проверка, что поле 'Логин' должно быть заполнено обязательно"""
    ep = EnterPage(browser)
    browser.find_element(*FirstPageLocators.PASSWORD_FIELD).send_keys('HowMathIsTheFish123')
    ep.should_be_a_required_login_field()


@pytest.mark.xfail(reason="The 'Password' field must be filled in")
def test_password_field_should_be_mandatory(browser):
    """Тесе-кейс №5 проверка,что поле 'Пароль' должно быть заполнено обязательно"""
    ep = EnterPage(browser)
    browser.find_element(*FirstPageLocators.LOGIN_FIELD).send_keys('My-Live')
    ep.should_be_a_required_password_field()
