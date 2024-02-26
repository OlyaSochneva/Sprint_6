from pages.main_page import MainPage


class CommonHeader(MainPage):
    def click_on_yandex_logo_and_switch_to_new_window(self, logo_locator, new_window_locator):
        self.switch_to_new_window_by_click_on_element(logo_locator)
        self.find_element_with_wait(new_window_locator)

    def return_to_main_page_by_click_on_logo(self, logo_locator, main_page_locator):
        self.click_and_wait_for(logo_locator, main_page_locator)
