import pytest
import allure
from pages.account_page import AccountPage
from pages.main_page import MainPage
from data import urls
from conftest import *
from data.urls import *

class TestAccount:
    @allure.title("Переход по клику на 'Личный кабинет'")
    def test_go_to_personal_account(self, driver):
        page = AccountPage(driver)
        page.go_to_base_url()
        page.click_profile_button()
        assert page.current_url() == LOGIN_PAGE_URL

    @allure.title('Переход в историю заказов')
    def test_open_history_order(self, driver, login_user):
        page = MainPage(driver)

        page.visible_button()

        page.go_to_profile_after_auth()
        page = AccountPage(driver)
        page.click_order_history()
        assert page.current_url() == USER_ACCOUNT_HISTORY_URL

    @allure.title('Выход из аккаунта')
    def test_logout_account(self, driver, login_user):
        page = MainPage(driver)

        page.visible_button()

        page.go_to_profile_after_auth()
        page = AccountPage(driver)
        page.logout()
        assert page.current_url() == LOGIN_PAGE_URL




