from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))

    def get_text(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def press_enter(self, locator):
        element = self.find_element_with_wait(locator)
        element.send_keys(Keys.ENTER)

    def fill_field(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def click_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def click_and_wait_for(self, locator, expected_element_locator):
        self.click_element(locator)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(expected_element_locator))

    def click_and_wait_for_close(self, locator):
        self.click_element(locator)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located(locator))

    def switch_to_new_window_by_click_on_element(self, locator):
        self.click_element(locator)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    @staticmethod
    def create_locator(raw_locator, index):
        method, locator = raw_locator
        locator = locator.format(index)
        well_done_locator = (method, locator)
        return well_done_locator

