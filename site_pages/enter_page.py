from .base_page import BasePage
from .locators import FirstPageLocators


class EnterPage(BasePage):
    def should_be_click_on_the_link_user_agreement(self):
        assert self.is_element_on_the_page(
            *FirstPageLocators.USER_AGREEMENT), 'User agreement field on the site is not presented'
        assert self.click_element(*FirstPageLocators.LINK_USER_AGREEMENT), 'Link user agreement is not presented'

    def checking_display_entered_data_in_login_fields(self):
        assert self.is_element_on_the_page(
            *FirstPageLocators.LOGIN_FIELD), 'The login field is not displayed on the login form'
        attr_login_fild = self.get_attr_element(*FirstPageLocators.LOGIN_FIELD, 'type')
        assert attr_login_fild == 'text', f"The login field has the type attribute {attr_login_fild}"

    def checking_display_entered_data_in_password_fields(self):
        assert self.is_element_on_the_page(
            *FirstPageLocators.PASSWORD_FIELD), 'The password field is not displayed on the login form'
        attr_password_fild = self.get_attr_element(*FirstPageLocators.PASSWORD_FIELD, 'type')
        assert attr_password_fild == 'password', f"The password field has the type attribute {attr_password_fild}"

    def should_be_click_on_the_button_enter_the_login_form(self):
        assert self.is_element_on_the_page(
            *FirstPageLocators.BUTTON_ENTER_LOGIN_FORM), "The button 'Enter' is not displayed on the login form"
        assert self.click_element(
            *FirstPageLocators.BUTTON_ENTER_LOGIN_FORM), "The button 'Enter' is not is not clickable"

    def should_be_a_required_login_field(self):
        assert self.browser.find_element(
            *FirstPageLocators.REQUIRED_LOGIN_FIELD), 'The login field is optional to fill in'

    def should_be_a_required_password_field(self):
        assert self.browser.find_element(
            *FirstPageLocators.REQUIRED_PASSWORD_FIELD), 'The password field is optional to fill in'
