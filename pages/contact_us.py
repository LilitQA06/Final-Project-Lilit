from locators.locators import LocatorsXPath
from selenium.webdriver.common.by import By


class ContactUs:

    def __init__(self, driver):
        self.driver = driver

        self.name = LocatorsXPath.name
        self.email = LocatorsXPath.email
        self.telephone = LocatorsXPath.telephone
        self.country = LocatorsXPath.country
        self.company = LocatorsXPath.company
        self.message = LocatorsXPath.message
        self.submit = LocatorsXPath.submit
        self.clear = LocatorsXPath.clear
        self.success_message_popup = LocatorsXPath.success_message_popup
        self.name_error_message_popup = LocatorsXPath.name_error_message_popup
        self.email_error_message_popup = LocatorsXPath.email_error_message_popup
        self.phone_number_error_message_popup = LocatorsXPath.phone_number_error_message_popup
        self.fill_name_input = LocatorsXPath.fill_name_input
        self.fill_email_input = LocatorsXPath.fill_email_input
        self.fill_phone_number = LocatorsXPath.fill_phone_number
        self.fill_country_name_input = LocatorsXPath.fill_country_name_input
        self.fill_company_name_input = LocatorsXPath.fill_company_name_input
        self.fill_message_input = LocatorsXPath.fill_message_input

    def set_input_name(self, text):
        input_name = self.driver.find_element_by_xpath(self.name)
        input_name.send_keys(text)

    def set_input_email(self, text):
        input_email = self.driver.find_element_by_xpath(self.email)
        input_email.send_keys(text)

    def set_input_phone_number(self, text):
        input_telephone = self.driver.find_element_by_xpath(self.telephone)
        input_telephone.send_keys(text)

    def set_input_country(self, text):
        input_country = self.driver.find_element_by_xpath(self.country)
        input_country.send_keys(text)

    def set_input_company(self, text):
        input_company = self.driver.find_element_by_xpath(self.company)
        input_company.send_keys(text)

    def set_input_message(self, text):
        input_message = self.driver.find_element_by_xpath(self.message)
        input_message.send_keys(text)

    def form_submit(self):
        submit_button = self.driver.find_element_by_xpath(self.submit)
        submit_button.click()

    def find_success_popup(self):
        return self.driver.find_element_by_xpath(self.success_message_popup)

    def find_name_error_popup(self):
        return self.driver.find_element_by_xpath(self.name_error_message_popup)


    def find_email_error_popup(self):
        return self.driver.find_element_by_xpath(self.email_error_message_popup)

    def find_phone_number_error_popup(self):
        return self.driver.find_element_by_xpath(self.phone_number_error_message_popup)
        

    def form_clear(self):
        clear_button = self.driver.find_element_by_xpath(self.clear)
        clear_button.click()

    def get_input_value(self, web_input):
        return self.driver.find_element(By.XPATH, web_input).get_attribute("value")
