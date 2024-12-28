import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Locators

class TestAccount():
    def test_account_open_from_main_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(by=By.XPATH, value=Locators.button_log_in_main_page).click()
        driver.find_element(by=By.XPATH, value=Locators.input_email).send_keys("artemkrutov17@gmail.com")
        driver.find_element(by=By.XPATH, value=Locators.input_pwd).send_keys("testpwd")
        driver.find_element(by=By.XPATH, value=Locators.button_enter).click()

        driver.find_element(by=By.XPATH, value=Locators.button_account).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locators.button_profile)
            )
        )

        driver.quit()

    @pytest.mark.parametrize(
        "buttons",
        (
            Locators.button_designer,
            Locators.logo,
        ),
        ids=(
            "by_designer",
            "by_logo",
        ),
    )
    def test_account_redirect_to_main_page(self, buttons):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(by=By.XPATH, value=Locators.button_log_in_main_page).click()
        driver.find_element(by=By.XPATH, value=Locators.input_email).send_keys("artemkrutov17@gmail.com")
        driver.find_element(by=By.XPATH, value=Locators.input_pwd).send_keys("testpwd")
        driver.find_element(by=By.XPATH, value=Locators.button_enter).click()

        driver.find_element(by=By.XPATH, value=Locators.button_account).click()

        driver.find_element(by=By.XPATH, value=buttons).click()
        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locators.text_make_burger)
            )
        )

        driver.quit()

    def test_account_log_out(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(by=By.XPATH, value=Locators.button_log_in_main_page).click()
        driver.find_element(by=By.XPATH, value=Locators.input_email).send_keys("artemkrutov17@gmail.com")
        driver.find_element(by=By.XPATH, value=Locators.input_pwd).send_keys("testpwd")
        driver.find_element(by=By.XPATH, value=Locators.button_enter).click()

        driver.find_element(by=By.XPATH, value=Locators.button_account).click()
        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locators.button_exit)
            )
        )
        driver.find_element(by=By.XPATH, value=Locators.button_exit).click()
        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locators.button_enter)
            )
        )

        driver.quit()
