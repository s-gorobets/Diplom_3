from locators.main_page_locator import *
from pages.base_page import Base_page
from pages.account_page import PersonalAccountLocators
import allure
from data.urls import *

class MainPage(Base_page):

    @allure.step("Переход на главную")
    def go_to_main(self):
        self.go_to_url(BASE_URL)
    @allure.step("Переход в раздел 'Конструктор'")
    def click_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BTN)

    @allure.step("Переход в раздел 'Лента заказов'")
    def click_order_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BTN)

    @allure.step("Вход в личный кабинет после авторизации")
    def go_to_profile_after_auth(self):
        self.forse_click(MainPageLocators.PROFILE_BTN)
        self.wait_for_visible(MainPageLocators.PROFILE_BTN)

    def visible_button(self):
        self.move_to_element(MainPageLocators.PROFILE_BTN)

    def go_to_feed(self):
        self.go_to_url(ORDER_FEED_URL)





