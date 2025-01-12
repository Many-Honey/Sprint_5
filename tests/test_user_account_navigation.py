from locators import Locators

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestUserAccountNavigation:


    def test_go_to_user_account_by_user_account_link_from_main_page(self, driver, reg_and_login):
        driver.find_element(*Locators.USER_ACCOUNT_LINK_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_INFO_TEXT))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quit()

    def test_go_to_burger_constructor_by_constructor_link_button(self, driver, reg_and_login):
        driver.find_element(*Locators.USER_ACCOUNT_LINK_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_INFO_TEXT))
        driver.find_element(*Locators.CONSTRUCTOR_LINK_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MAKE_BURGER_HEADER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_go_to_burger_constructor_by_stellar_burgers_logo(self, driver, reg_and_login):
        driver.find_element(*Locators.USER_ACCOUNT_LINK_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_INFO_TEXT))
        driver.find_element(*Locators.STELLAR_BURGERS_LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MAKE_BURGER_HEADER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_logout_from_user_account(self, driver, reg_and_login):
        driver.find_element(*Locators.USER_ACCOUNT_LINK_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_INFO_TEXT))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()


