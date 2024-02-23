from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from locators.common_header_locators import CommonHeaderLocators


class MainPage(BasePage):

    def click_on_question_and_get_answer_text(self, question_locator, answer_locator, number):
        question_locator = self.create_locator(question_locator, number)
        answer_locator = self.create_locator(answer_locator, number)
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        return self.get_text(answer_locator)

    def click_on_order_button(self, button):
        if button == CommonHeaderLocators.HEADER_ORDER_BUTTON:
            self.click_and_wait_for(button, OrderPageLocators.NEXT_BUTTON)
        if button == MainPageLocators.ORDER_BUTTON:
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON)
            self.click_and_wait_for(button, OrderPageLocators.NEXT_BUTTON)


