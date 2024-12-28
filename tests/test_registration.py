from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Locators

class TestRegistration():

    def test_registration_user_already_exists(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.button_reg)))

        driver.find_element(by=By.XPATH, value=Locators.input_name).send_keys("name")
        driver.find_element(by=By.XPATH, value=Locators.input_email).send_keys("123@ya.ru")
        driver.find_element(by=By.XPATH, value=Locators.input_pwd).send_keys("123456")
        driver.find_element(by=By.XPATH, value=Locators.button_reg).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, Locators.err_validation), "Такой пользователь уже существует")
        )

        driver.quit()


    def test_registration_user_pwd_len_err(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.button_reg)))

        driver.find_element(by=By.XPATH, value=Locators.input_name).send_keys("name")
        driver.find_element(by=By.XPATH, value=Locators.input_email).send_keys("123@ya.ru")
        driver.find_element(by=By.XPATH, value=Locators.input_pwd).send_keys("123")
        driver.find_element(by=By.XPATH, value=Locators.button_reg).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.XPATH, Locators.err_validation), "Некорректный пароль"
            )
        )

        driver.quit()
