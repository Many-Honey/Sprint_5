from locators import Locators

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginPage:

    def test_log_in_by_log_in_to_account_button_main_page(self,driver, registration, registration_dict):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(registration_dict['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(registration_dict['password'])
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_BURGER_HEADER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed() == True
        driver.quit()


    def test_log_in_by_profile_link_button_main_page(self,driver, registration_dict, registration):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.USER_ACCOUNT_LINK_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(registration_dict['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(registration_dict['password'])
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_BURGER_HEADER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(
            *Locators.MAKE_ORDER_BUTTON).is_displayed() == True
        driver.quit()



    def test_log_in_by_log_in_link_registration_page(self, driver, registration_dict, registration):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(registration_dict['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(registration_dict['password'])
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_BURGER_HEADER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(
            *Locators.MAKE_ORDER_BUTTON).is_displayed() == True
        driver.quit()

    def test_log_in_by_log_in_link_password_recovery_page(self, driver, registration, registration_dict):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(registration_dict['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(registration_dict['password'])
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_BURGER_HEADER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(
            *Locators.MAKE_ORDER_BUTTON).is_displayed() == True
        driver.quit()

