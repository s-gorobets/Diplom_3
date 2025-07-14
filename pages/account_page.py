from locators.account_login_page_locator import *
from locators.main_page_locator import *

from pages.base_page import Base_page
import allure
from data.urls import *
from data.data import email, password

class AccountPage(Base_page):

    @allure.step("Переход на главную")
    def go_to_base_url(self):
        self.go_to_url(BASE_URL)

    @allure.step("Ожидание кнопки Личный кабинет")
    def wait_profile_button(self):
        self.wait_for_visible(PersonalAccountLocators.PROFILE_BTN)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_profile_button(self):
        self.forse_click(PersonalAccountLocators.PROFILE_BTN)

    @allure.step("Авторизация")
    def login_in_account(self, email, password):
        self.wait_for_visible(PersonalAccountLocators.EMAIL_FIELD)
        self.add_text_element(PersonalAccountLocators.EMAIL_FIELD, email)
        self.add_text_element(PersonalAccountLocators.PASSWORD_FIELD, password)
        self.move_to_element(PersonalAccountLocators.ENTER_BTN)
        self.forse_click(PersonalAccountLocators.ENTER_BTN)

    @allure.step("Переход в профиль")
    def go_to_profile(self):
        self.forse_click(MainPageLocators.PROFILE_BTN)

    @allure.step("Переход в историю заказов")
    def click_order_history(self):
        self.forse_click(PersonalAccountLocators.ORDER_HISTORY_BTN)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.forse_click(PersonalAccountLocators.LOGOUT_BTN)
        self.wait_for_invisible(PersonalAccountLocators.LOGOUT_BTN)
