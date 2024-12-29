from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Locators, Urls, Data, Errors

class TestRegistration:

    def test_registration_user_already_exists(self, driver):
        driver.get(Urls.REG_PAGE)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BUTTON_REG))

        driver.find_element(*Locators.INPUT_NAME).send_keys(Data.NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.REG_EMAIL)
        driver.find_element(*Locators.INPUT_PWD).send_keys(Data.VALID_PWD)
        driver.find_element(*Locators.BUTTON_REG).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.text_to_be_present_in_element(
                (Locators.ERR_VALIDATION), Errors.USER_ALREADY_EXIST
            )
        )

    def test_registration_user_pwd_len_err(self, driver):
        driver.get(Urls.REG_PAGE)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BUTTON_REG))

        driver.find_element(*Locators.INPUT_NAME).send_keys(Data.NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.REG_EMAIL)
        driver.find_element(*Locators.INPUT_PWD).send_keys(Data.SHORT_PWD)
        driver.find_element(*Locators.BUTTON_REG).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.text_to_be_present_in_element(
                (Locators.ERR_VALIDATION), Errors.WRONG_PWD
            )
        )

