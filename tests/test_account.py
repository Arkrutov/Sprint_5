import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Locators, Urls, Data

class TestAccount:
    def test_account_open_from_main_page(self, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*Locators.BUTTON_LOG_IN_MAIN_PAGE).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.LOGIN)
        driver.find_element(*Locators.INPUT_PWD).send_keys(Data.PWD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

        driver.find_element(*Locators.BUTTON_ACCOUNT).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (Locators.BUTTON_PROFILE)
            )
        )


    @pytest.mark.parametrize(
        "buttons",
        (
            Locators.BUTTON_DESIGNER,
            Locators.LOGO,
        ),
        ids=(
            "by_designer",
            "by_logo",
        ),
    )
    def test_account_redirect_to_main_page(self, buttons, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*Locators.BUTTON_LOG_IN_MAIN_PAGE).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.LOGIN)
        driver.find_element(*Locators.INPUT_PWD).send_keys(Data.PWD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

        driver.find_element(*Locators.BUTTON_ACCOUNT).click()

        driver.find_element(*buttons).click()
        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (Locators.TEXT_MAKE_BURGER)
            )
        )


    def test_account_log_out(self, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*Locators.BUTTON_LOG_IN_MAIN_PAGE).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.LOGIN)
        driver.find_element(*Locators.INPUT_PWD).send_keys(Data.PWD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

        driver.find_element(*Locators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (Locators.BUTTON_EXIT)
            )
        )
        driver.find_element(*Locators.BUTTON_EXIT).click()
        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (Locators.BUTTON_ENTER)
            )
        )

