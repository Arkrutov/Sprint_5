from selenium.webdriver.common.by import By
from selenium import webdriver

from constants import Locators

class TestDesigner():

    def test_designer_check_tabs(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        locators = [Locators.button_filling, Locators.button_sauce, Locators.button_rolls]

        for locator in locators:
            driver.find_element(by=By.XPATH, value=locator).click()
            current_class = driver.find_element(by=By.XPATH, value=locator).get_attribute('class')
            assert "tab_tab_type_current" in current_class

        driver.quit()