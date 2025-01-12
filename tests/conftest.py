import random
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


@pytest.fixture
def random_email_generator():
    email = f'masha_shegai_{random.randint(10, 99)}_{random.randint(100, 999)}@yandex.ru'
    return email

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@pytest.fixture
def registration_dict(random_email_generator):
    reg_dict = {'email': random_email_generator, 'password': '123456', 'name': 'Maria'}
    return reg_dict

@pytest.fixture
def registration(registration_dict, driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.NAME_FIELD_REG).send_keys(registration_dict['name'])
    driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(registration_dict['email'])
    driver.find_element(*Locators.PASSWORD_FIELD_REG).send_keys(registration_dict['password'])
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    return driver

@pytest.fixture
def reg_and_login(driver, registration_dict):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.NAME_FIELD_REG).send_keys(registration_dict['name'])
    driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(registration_dict['email'])
    driver.find_element(*Locators.PASSWORD_FIELD_REG).send_keys(registration_dict['password'])
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
    driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(registration_dict['email'])
    driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(registration_dict['password'])
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver

