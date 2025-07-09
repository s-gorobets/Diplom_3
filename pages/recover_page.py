from locators.recover_pass_page_locator import *
from pages.base_page import Base_page
import allure
from data.urls import *
from conftest import create_user_and_delete

class RecoverPage(Base_page):
    @allure.step("Переход на страницу восстановления пароля")
    def go_recover_pass_link(self):
        self.go_to_url(RESTORE_PASSWORD_URl)

    @allure.step("Переход на страницу входа")
    def go_login_pass_link(self):
        self.go_to_url(LOGIN_PAGE_URL)

    @allure.step("Клик на кнопку восстановления пароля ")
    def clicl_btn_recover_pass(self):
        self.click(RecoverPass.RECOVER_PASS_BTN)

    @allure.step("Получить урл страницы восстановления")
    def get_url_recover(self):
        return self.current_url()

    allure.step("Ввод email и клик по кнопке Восстановить")
    def click_and_input_email_pass(self, email):
        self.click_on_element(RecoverPass.EMAIL_INPUT)
        self.add_text_element(RecoverPass.EMAIL_INPUT, email)
        self.click_on_element(RecoverPass.RECOVER_BTN)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def toggle_show_pass(self):
        self.click_on_element(RecoverPass.SHOW_PASS_TOGGLE)

    @allure.step("Видимость поля")
    def is_pass_field_activ(self):
        self.is_visible_element(RecoverPass.PASSWORD_FIELD_IS_ACTIVE)




