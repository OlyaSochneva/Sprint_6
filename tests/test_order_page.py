import pytest
import allure

from selenium.webdriver.support import expected_conditions

from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.common_header_locators import CommonHeaderLocators

from data import User


class TestOrderPage:
    @pytest.mark.parametrize(
        "button, user",
        [
            (MainPageLocators.ORDER_BUTTON, User.FIRST_DATA_SET),
            (CommonHeaderLocators.HEADER_ORDER_BUTTON, User.SECOND_DATA_SET)
        ])
    @allure.title('Проверка: при прохождении всего позитивного сценария с корректными данными заказ успешно создаётся')
    def test_create_order(self, main_page, order_page, button, user):
        main_page.click_on_order_button(button)
        order_page.create_order(
            OrderPageLocators.INPUT_FIELDS, OrderPageLocators.STATION,
            OrderPageLocators.RENTAL_TERM_INPUT_FIELD, OrderPageLocators.AMOUNT_OF_DAYS, user)
        assert expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_CONFIRM_WINDOW)
