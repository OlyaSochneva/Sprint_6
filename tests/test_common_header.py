import allure

from selenium.webdriver.support import expected_conditions

from locators.main_page_locators import MainPageLocators
from locators.common_header_locators import CommonHeaderLocators


class TestCommonHeader:
    @allure.title('Проверка: при нажатии на лого Яндекса в новом окне откроется главная Дзена')
    def test_redirect_by_click_on_yandex_logo(self, common_header):
        common_header.click_on_yandex_logo_and_switch_to_new_window(
            CommonHeaderLocators.YANDEX_LOGO, CommonHeaderLocators.DZEN_LOGO)
        assert expected_conditions.visibility_of_element_located(CommonHeaderLocators.DZEN_LOGO)

    @allure.title('Проверка: при нажатии на лого Самоката произойдёт переход на главную страницу')
    def test_return_to_main_page_by_click_on_scooter_logo(self, common_header):
        common_header.click_on_order_button(CommonHeaderLocators.HEADER_ORDER_BUTTON)
        common_header.return_to_main_page_by_click_on_logo(
            CommonHeaderLocators.SCOOTER_LOGO, MainPageLocators.ORDER_BUTTON)
        assert expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
