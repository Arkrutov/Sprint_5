import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Locators

class TestLogIn():

    @pytest.mark.parametrize(
        "pages, locators",
        [
            ("https://stellarburgers.nomoreparties.site/", Locators.button_log_in_main_page),
            ("https://stellarburgers.nomoreparties.site/login", Locators.button_account),
            ("https://stellarburgers.nomoreparties.site/register", Locators.button_enter_from_page),
            ("https://stellarburgers.nomoreparties.site/forgot-password", Locators.button_enter_from_page),
        ],
        ids=(
            "main",
            "account",
            "registration",
            "forgot-password",
        ),
    )
    def test_log_in_from_forgot_pwd_page_p(self, pages, locators):
        driver = webdriver.Chrome()
        driver.get(pages)

        driver.find_element(by=By.XPATH, value=locators).click()

        driver.find_element(by=By.XPATH, value=Locators.input_email).send_keys("artemkrutov17@gmail.com")
        driver.find_element(by=By.XPATH, value=Locators.input_pwd).send_keys("testpwd")
        driver.find_element(by=By.XPATH, value=Locators.button_enter).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locators.button_order)
            )
        )

        driver.quit()
