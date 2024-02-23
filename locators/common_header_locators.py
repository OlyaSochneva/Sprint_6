from selenium.webdriver.common.by import By


class CommonHeaderLocators:
    # Кнопка «Заказать» в хэдере:
    HEADER_ORDER_BUTTON = By.XPATH, '// div[contains(@class, "Header")]/child::button[text()="Заказать"]'

    # лого Яндекса:
    YANDEX_LOGO = By.XPATH, '// *[@href="//yandex.ru"]'

    # лого Самоката:
    SCOOTER_LOGO = By.XPATH, '// *[contains(@class, "LogoScooter")]'

    # лого Дзена (на стр дзена):
    DZEN_LOGO = By.XPATH, '// a[@aria-label="Логотип Бренда"]'

