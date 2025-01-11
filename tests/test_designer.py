from constants import Locators, Urls

class TestDesigner:

    def test_designer_check_tabs(self, driver):
        driver.get(Urls.MAIN_PAGE)

        locators = [Locators.BUTTON_FILLING, Locators.BUTTON_SAUCE, Locators.BUTTON_ROLLS]

        for locator in locators:
            driver.find_element(*locator).click()
            current_class = driver.find_element(*locator).get_attribute('class')
            assert "tab_tab_type_current" in current_class
