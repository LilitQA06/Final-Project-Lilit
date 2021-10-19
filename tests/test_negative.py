from pages.base_page import Base
import pytest
from pages.contact_us import ContactUs
from time import sleep
from selenium.webdriver.common.by import By





# Negative - check that the name field contains only letters and is not empty
@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    @pytest.mark.parametrize("name_input", ["111111", "!@#$%^&*()_+", "  ", ""])
    def test_name_field(self, name_input):
        driver = self.driver
        contact = ContactUs(driver)
        contact.set_input_name(name_input)
        contact.set_input_email("test@test.com")
        contact.set_input_phone_number("+37493489961")
        contact.set_input_country("Armenia")
        contact.set_input_company("BluNet")
        contact.set_input_message("text")
        contact.form_submit()
        assert contact.find_name_error_popup(), "Error message popup doesn't exist"
        sleep(3)

    # Negative - check that the email is valid
    @pytest.mark.parametrize("email_input", ["nn", "n@", "  ", ""])
    def test_email_field(self, email_input):
        driver = self.driver
        contact = ContactUs(driver)
        contact.set_input_name("Test")
        contact.set_input_email(email_input)
        contact.set_input_phone_number("+37493489961")
        contact.set_input_country("Armenia")
        contact.set_input_company("BluNet")
        contact.set_input_message("text")
        contact.form_submit()
        assert contact.find_email_error_popup, "Error message popup doesn't exist"
        sleep(3)

# Negative - phone only digits, not letters, not empty
@pytest.mark.parametrize("phone_number_input", ["asdasd", "!@#$%", "  ", ""])
def test_phone_number_field(self, phone_number_input):
        driver = self.driver
        contact = ContactUs(driver)
        contact.set_input_name("Test")
        contact.set_input_email("test@test.com")
        contact.set_input_phone_number(phone_number_input)
        contact.set_input_country("Armenia")
        contact.set_input_company("BluNet")
        contact.set_input_message("Some text")
        contact.form_submit()
        assert contact.find_phone_number_error_popup, "Error message popup doesn't exist"
        sleep(3)

     
# Negative - Country only letters and spaces
@pytest.mark.parametrize("country_input", ["111111", "~!@#$%^&*()_+ ", " ", ""])
def test_phone_number_field(self, country_input):
        driver = self.driver
        contact = ContactUs(driver)
        contact.set_input_name("test")
        contact.set_input_email("test@test.com")
        contact.set_input_phone_number("+37493489961")
        contact.set_input_country(country_input)
        contact.set_input_company("BluNet")
        contact.set_input_message("Some text")
        contact.form_submit()
        assert country_input != ' ' and country_input != '' and all(chr.isalpha() or chr.isspace() for chr in country_input), "Error message popup doesn't exist"
        
        sleep(3)


# Negative- Message cannot have more than 180 letters, can be empty
@pytest.mark.parametrize("message_input", ["","181asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasda"])
def test_message_field(self, message_input):
        driver = self.driver
        contact = ContactUs(driver)
        contact.set_input_name("Test")
        contact.set_input_email("test@gmail.com")
        contact.set_input_phone_number("+37493489961")
        contact.set_input_country("Armenia")
        contact.set_input_company("BluNet")
        contact.set_input_message(message_input)
        assert len(message_input) <= 180, "Can not contain more than 180 letters"
        contact.form_submit()
        sleep(3)