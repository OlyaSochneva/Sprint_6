import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from pages.common_header import CommonHeader
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(scope="function")
def driver():
    my_options = Options()
    service = Service(executable_path="/Users/olyasochneva/Downloads/WebDriverF/bin/geckodriver")
    my_options.add_argument("--width=1920")
    my_options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=my_options, service=service)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope="function")
def order_page(driver):
    return OrderPage(driver)


@pytest.fixture(scope="function")
def common_header(driver):
    return CommonHeader(driver)
