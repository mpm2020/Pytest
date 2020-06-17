from Pages.BaseApp import BasePage


class FormLocators:
    LOCATOR_NAME_FIELD = "//*[@id='formEmployee']/div[2]/div[1]/input"
    LOCATOR_EMAIL_FIELD = "//*[@id='formEmployee']/div[2]/div[2]/input"
    LOCATOR_ADDRESS_FIELD = "address"
    LOCATOR_PHONE_FIELD = "phone"
    LOCATOR_ADD_BUTTON = "addButton"

class form(BasePage):

    def register_data(self):
        name_field = self.driver.find_element_by_xpath(FormLocators.LOCATOR_NAME_FIELD)
        name_field.send_keys("mariana montenegro")
        email_field = self.driver.find_element_by_xpath(FormLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys("mariana.montenegro77@gmail.com")
        address_field = self.driver.find_element_by_id(FormLocators.LOCATOR_ADDRESS_FIELD)
        address_field.send_keys("GREGORIO CARRERAS 2553")
        phone_field = self.driver.find_element_by_id(FormLocators.LOCATOR_PHONE_FIELD)
        phone_field.send_keys("152316521")
        add_btn = self.driver.find_element_by_id(FormLocators.LOCATOR_ADD_BUTTON)
        #add_btn.click()