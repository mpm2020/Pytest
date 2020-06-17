from Pages.BaseApp import BasePage


class LoginLocators:
    LOCATOR_USERNAME_FIELD = "user"
    LOCATOR_PASSWORD_FIELD = "pass"
    LOCATOR_SIGNON_BUTTON = "loginButton"


class login(BasePage):

    def enter_credentials(self):
        user_field = self.driver.find_element_by_id(LoginLocators.LOCATOR_USERNAME_FIELD)
        user_field.send_keys("Admin")
        pass_field = self.driver.find_element_by_id(LoginLocators.LOCATOR_PASSWORD_FIELD)
        pass_field.send_keys("admin123")
        login_btn = self.driver.find_element_by_id(LoginLocators.LOCATOR_SIGNON_BUTTON)
        login_btn.click()
