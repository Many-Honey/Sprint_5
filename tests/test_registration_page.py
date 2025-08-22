from locators import Locators
from urls import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistrationPage:


    def test_successful_registration(self, registration_dict, driver):
        driver.get(registration_page)
        driver.find_element(*Locators.NAME_FIELD_REG).send_keys(registration_dict['name'])
        driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(registration_dict['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_REG).send_keys(registration_dict['password'])
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER))
        assert '/login' in driver.current_url
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(registration_dict['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(registration_dict['password'])
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MAKE_BURGER_HEADER))
        assert driver.current_url == main_page and driver.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed() == True

    def test_input_password_less_than_6_characters_error_message(self, registration_dict, driver):
        password = 123
        driver.get(registration_page)
        driver.find_element(*Locators.NAME_FIELD_REG).send_keys(registration_dict['name'])
        driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(registration_dict['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_REG).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert driver.current_url == registration_page and driver.find_element(*Locators.PASSWORD_ERROR_MESSAGE).is_displayed()

