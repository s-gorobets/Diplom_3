import pytest
import allure
from pages.recover_page import RecoverPage
from data import urls
from conftest import *
from data.urls import *
class TestPasswordRecoveryFlow:
    @allure.step('Переход на страницу восстановления пароля')
    def test_go_to_page_recovery(self, driver):
        page = RecoverPage(driver)
        page.go_login_pass_link()
        page.clicl_btn_recover_pass()
        assert page.get_url_recover() == RESTORE_PASSWORD_URl

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_push_restore(self, driver, create_user_and_delete):
        user_emeil = create_user_and_delete['email']
        page = RecoverPage(driver)
        page.go_recover_pass_link()
        page.click_and_input_email_pass(user_emeil)
        assert page.is_pass_field_activ

    @allure.title("Клик по кнопке показать/скрыть пароль активирует поле")
    def test_show_hide_pass(self, driver, create_user_and_delete):
        page = RecoverPage(driver)
        page.go_recover_pass_link()
        email = create_user_and_delete['email']
        page.click_and_input_email_pass(email)
        page.toggle_show_pass()
        assert page.is_pass_field_activ

