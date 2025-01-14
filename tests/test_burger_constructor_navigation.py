import time
from locators import Locators
from urls import *



class TestBurgerConstructorNavigation:


    def test_go_to_fillings_section_by_click_on_fillings(self, driver):
        driver.get(main_page)
        filling_section = driver.find_element(*Locators.FILLINGS_SECTION)
        filling_section.click()
        assert 'tab_tab_type_current__2BEPc' in filling_section.get_attribute('class')

    def test_go_to_buns_section_by_click_on_buns(self, driver):
        driver.get(main_page)
        driver.find_element(*Locators.FILLINGS_SECTION).click()
        time.sleep(1)
        buns_section = driver.find_element(*Locators.BUNS_SECTION)
        buns_section.click()
        time.sleep(1)
        assert 'tab_tab_type_current__2BEPc' in buns_section.get_attribute('class')

    def test_go_to_sauces_section_by_click_on_sauces(self, driver):
        driver.get(main_page)
        sauces_section = driver.find_element(*Locators.SAUCES_SECTION)
        sauces_section.click()
        assert 'tab_tab_type_current__2BEPc' in sauces_section.get_attribute('class')


