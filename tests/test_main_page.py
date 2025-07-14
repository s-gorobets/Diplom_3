import pytest
import allure
from pages.main_page import MainPage
from conftest import *
from data.urls import *

class TestMainPage:
    @allure.title("Переход по клику на 'Конструктор'")
    def test_click_constructor(self, driver):
        page = MainPage(driver)
        page.go_to_main()
        page.click_constructor()
        assert page.current_url() == BASE_URL

    @allure.title("Переход по клику на 'Ленту заказов'")
    def test_click_order_feed(self,driver):
        page = MainPage(driver)
        page.go_to_main()
        page.click_order_feed()
        assert page.current_url() == ORDER_FEED_URL

    @allure.title("При клике на игридиент открывается модалка")
    def test_igridient_modal_open(self, driver):
        page = ConstructorPage(driver)
        page.go_to_main()
        page.click_ingredient()
        assert page.is_ingredient_details_modal_visible()

    @allure.title("Модалка закрывается по клику на крестик")
    def test_close_modal_igridient(self,driver):
        page = ConstructorPage(driver)
        page.go_to_main()
        page.click_ingredient()
        page.is_ingredient_details_modal_visible()
        assert page.close_modal()

    @allure.title("Добавление ингредиента увеличивает счётчик")
    def test_add_ingredient_counter_increases(self, driver):
        page = ConstructorPage(driver)
        page.go_to_main()
        page.add_ingredient_to_order()
        count = page.get_ingredient_counter()
        assert count == '2'

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_order_submit(self, driver, login_user):
        constructor = ConstructorPage(driver)
        constructor.create_an_order()
        assert constructor.is_order_preparing_message_visible




