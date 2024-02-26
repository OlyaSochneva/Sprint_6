from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка «Заказать» внутри главной страницы:
    ORDER_BUTTON = By.XPATH, '// div[contains(@class, "FinishButton")]/child::button'

    # общий локатор для вопросов:
    QUESTION = By.ID, 'accordion__heading-{}'

    # общий локатор для ответов:
    ANSWER = By.ID, 'accordion__panel-{}'












