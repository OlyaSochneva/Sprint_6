from selenium.webdriver.common.by import By


class OrderPageLocators:
    # общий локатор для полей ввода:
    INPUT_FIELDS = By.XPATH, '// input[@placeholder="* {}"]'

    # общий локатор для станций:
    STATION = By.XPATH, '// div[text()="{}"]/parent::button'

    # кнопка «Далее» на стр «Для кого самокат»:
    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'

    # поле «Срок аренды» на стр «Про аренду»:
    RENTAL_TERM_INPUT_FIELD = By.XPATH, '// div[contains(@class, "Dropdown-control")]'

    # общий локатор для пунктов выпадающего списка «Срок аренды»:
    AMOUNT_OF_DAYS = By.XPATH, '// div[@role="option" and text()="{}"]'

    # Кнопка «Заказать» на стр «Про аренду»:
    ORDER_BUTTON = By.XPATH, '// div[contains(@class, "Order_Buttons")]/child::button[text()="Заказать"]'

    # Кнопка «Да» в окне подтверждения заказа:
    ORDER_CONFIRM_YES = By.XPATH, '//button[text()="Да"]'

    # Окно «Заказ оформлен»:
    ORDER_CONFIRM_WINDOW = By.XPATH, '// div[text()="Заказ оформлен"]'
