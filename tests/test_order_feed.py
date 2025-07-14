import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from conftest import *
from data.urls import *

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Клик по заказу открывает модалку с деталями")
    def test_click_order_opens_modal(self, driver):
        page = MainPage(driver)
        page.go_to_main()
        page.click_order_feed()
        page = OrderPage(driver)
        page.click_on_order()
        assert page.is_order_modal_visible()

    @allure.title("Заказы пользователя из истории отображаются в ленте заказов")
    def test_user_orders_displayed(self, driver, create_order):
        order_number = create_order
        page = MainPage(driver)
        page.go_to_main()
        page.click_order_feed()
        page = OrderPage(driver)
        assert page.is_order_number_in_work_displayed(order_number = order_number)

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается")
    def test_total_orders_counter_increases(self, driver, create_user_and_delete):
        user_email = create_user_and_delete["email"]
        user_password = create_user_and_delete["password"]

        page = MainPage(driver)
        page.go_to_main()
        page.click_order_feed()

        page = OrderPage(driver)
        page.go_order_feed()
        total_order = page.get_total_orders_all_time()

        page = AccountPage(driver)
        page.go_to_profile()
        page.login_in_account(user_email, user_password)


        page = ConstructorPage(driver)
        page.create_an_order()

        page = MainPage(driver)
        page.go_to_main()
        page.click_order_feed()

        page = OrderPage(driver)
        now_total_order = page.get_total_orders_all_time()

        assert total_order < now_total_order

    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_total_orders_counter_increases(self, driver, create_user_and_delete):
        user_email = create_user_and_delete["email"]
        user_password = create_user_and_delete["password"]

        page = MainPage(driver)
        page.go_to_main()
        page.click_order_feed()

        page = OrderPage(driver)
        page.go_order_feed()
        total_order = page.get_total_orders_all_time()

        page = AccountPage(driver)
        page.go_to_profile()
        page.login_in_account(user_email, user_password)

        page = ConstructorPage(driver)
        page.create_an_order()

        page = MainPage(driver)
        page.go_to_main()
        page.click_order_feed()

        page = OrderPage(driver)
        now_total_order = page.get_total_orders_all_time()

        assert total_order < now_total_order

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_create_order_number_in_feed_list(self, driver, login_user):
        page = ConstructorPage(driver)
        order_number = page.create_an_order()
        page = MainPage(driver)
        page.click_order_feed()
        page = OrderPage(driver)
        assert page.is_order_number_in_work_displayed(order_number)