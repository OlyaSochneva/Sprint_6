import pytest
import allure

from locators.main_page_locators import MainPageLocators

from answers import Answers



class TestMainPage:
    @pytest.mark.parametrize(
        "index, expected_answer",
        [
            (0, Answers.COST_AND_PAYMENT),
            (1, Answers.MORE_SCOOTERS),
            (2, Answers.RENTAL_TIME),
            (3, Answers.TODAY_DELIVERY),
            (4, Answers.EXTEND_RETURN),
            (5, Answers.ABOUT_CHARGER),
            (6, Answers.CANCEL_ORDER),
            (7, Answers.FAR_AWAY_DELIVERY)
        ])
    @allure.title('Проверка: при нажатии на вопрос появляется правильный текст ответа')
    def test_info(self, main_page, index, expected_answer):
        result = main_page.click_on_question_and_get_answer_text(
            MainPageLocators.QUESTION, MainPageLocators.ANSWER, index)
        assert result == expected_answer
