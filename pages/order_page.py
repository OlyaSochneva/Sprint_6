from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def create_order(self, fields_locator, station_locator, rental_term_field_locator, amount_of_days_locator, data_set):
        self.who_orders_fill_fields_and_next(fields_locator, station_locator, data_set)
        self.about_rent_fill_fields_and_order(fields_locator, rental_term_field_locator,
                                              amount_of_days_locator, data_set)

    def who_orders_fill_fields_and_next(self, fields_locator, station_locator, data_set):
        self.fill_name_field(fields_locator, data_set)
        self.fill_surname_field(fields_locator, data_set)
        self.fill_address_field(fields_locator, data_set)
        self.choose_the_station(fields_locator, station_locator, data_set)
        self.fill_phone_number_field(fields_locator, data_set)
        self.click_and_wait_for_close(OrderPageLocators.NEXT_BUTTON)

    def about_rent_fill_fields_and_order(self, fields_locator, rental_term_field_locator,
                                         amount_of_days_locator, data_set):
        self.fill_delivery_date(fields_locator, data_set)
        self.choose_rental_term(rental_term_field_locator, amount_of_days_locator, data_set)
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.ORDER_CONFIRM_YES)

    def fill_name_field(self, common_locator, data_set):
        field_locator = self.create_locator(common_locator, "Имя")
        name = data_set.get('name')
        self.fill_field(field_locator, name)

    def fill_surname_field(self, common_locator, data_set):
        field_locator = self.create_locator(common_locator, "Фамилия")
        surname = data_set.get('surname')
        self.fill_field(field_locator, surname)

    def fill_address_field(self, common_locator, data_set):
        field_locator = self.create_locator(common_locator, "Адрес: куда привезти заказ")
        address = data_set.get('address')
        self.fill_field(field_locator, address)

    def choose_the_station(self, common_locator, station_locator, data_set):
        field_locator = self.create_locator(common_locator, "Станция метро")
        station_index = data_set.get('station')
        station_locator = self.create_locator(station_locator, station_index)
        self.click_element(field_locator)
        self.click_and_wait_for_close(station_locator)

    def fill_phone_number_field(self, common_locator, data_set):
        field_locator = self.create_locator(common_locator, "Телефон: на него позвонит курьер")
        phone_number = data_set.get('phone_number')
        self.fill_field(field_locator, phone_number)

    def fill_delivery_date(self, common_locator, data_set):
        field_locator = self.create_locator(common_locator, "Когда привезти самокат")
        delivery_date = data_set.get('delivery_date')
        self.fill_field(field_locator, delivery_date)
        self.press_enter(field_locator)

    def choose_rental_term(self, rental_term_field_locator, amount_of_days_locator, data_set):
        index = data_set.get('amount_of_days')
        amount_of_days_locator = self.create_locator(amount_of_days_locator, index)
        self.click_element(rental_term_field_locator)
        self.click_and_wait_for_close(amount_of_days_locator)
