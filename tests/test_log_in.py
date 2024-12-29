import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Locators, Urls, Data

class TestLogIn:

    @pytest.mark.parametrize(
        "pages, locators",
        [
            (Urls.MAIN_PAGE, Locators.BUTTON_LOG_IN_MAIN_PAGE),
            (Urls.LOGIN_PAGE, Locators.BUTTON_ACCOUNT),
            (Urls.REG_PAGE, Locators.BUTTON_ENTER_FROM_PAGE),
            (Urls.FORGOT_PWD_PAGE, Locators.BUTTON_ENTER_FROM_PAGE),
        ],
        ids=(
            "main",
            "account",
            "registration",
            "forgot-password",
        ),
    )
    def test_log_in_from_forgot_pwd_page_p(self, pages, locators, driver):
        driver.get(pages)

        driver.find_element(*locators).click()

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.LOGIN)
        driver.find_element(*Locators.INPUT_PWD).send_keys(Data.PWD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (Locators.BUTTON_ORDER)
            )
        )

