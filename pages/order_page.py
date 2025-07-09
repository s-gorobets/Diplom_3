from locators.order_page_locator import *
from pages.base_page import Base_page
import allure
from data.urls import *

class OrderPage(Base_page):
    @allure.step("Клик по заказу в ленте")
    def click_on_order(self):
        self.click(OrderFeedPageLocators.ORDER_IN_FEED_LINK)

    @allure.step("Проверка отображения модального окна заказа")
    def is_order_modal_visible(self):
        return self.is_visible_element(OrderFeedPageLocators.ORDER_MODAL_CONTENTS_TITLE)

    @allure.step("Получение счётчика 'Выполнено за сегодня'")
    def get_total_orders_today(self):
        return int(self.get_text_element(OrderFeedPageLocators.COMPLETE_ORDERS_TODAY_COUNTER))

    @allure.step("Получение счётчика 'Выполнено за всё время'")
    def get_total_orders_all_time(self):
        return int(self.get_text_element(OrderFeedPageLocators.COMPLETE_ORDERS_TOTAL_COUNTER))

    @allure.step("Проверка отображения номера заказа в работе")
    def is_order_number_in_work_displayed(self, order_number):
        locator = OrderFeedPageLocators.get_order_in_order_feed(order_number)
        return self.is_visible_element(locator)

    @allure.step("Переход в раздел 'Лента заказов'")
    def go_order_feed(self):
        self.click_on_element(OrderFeedPageLocators.ORDER_IN_FEED_LINK)