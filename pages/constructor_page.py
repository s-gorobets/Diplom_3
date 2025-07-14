from locators.constructor_page_locator import *
from pages.base_page import Base_page
import allure
from data.urls import *

class ConstructorPage(Base_page):

        @allure.step("Переход на главную")
        def go_to_main(self):
            self.go_to_url(BASE_URL)

        @allure.step("Клик по ингредиенту")
        def click_ingredient(self):
            self.forse_click(ConstructorPageLocators.INGREDIENT_BUN)

        @allure.step("Проверка отображения модального окна с деталями")
        def is_ingredient_details_modal_visible(self):
            return self.is_visible_element(ConstructorPageLocators.INGREDIENT_DETAILS_MODAL_TITLE)

        @allure.step("Закрытие модального окна")
        def close_modal(self):
            self.click(ConstructorPageLocators.MODAL_CLOSE_BTN)
            return self.wait_for_invisible(ConstructorPageLocators.INGREDIENT_DETAILS_MODAL_TITLE)

        @allure.step("Получение счётчика ингредиента")
        def get_ingredient_counter(self):
            return self.get_text_element(ConstructorPageLocators.INGREDIENT_COUNTER)

        @allure.step("Добавление ингредиента в заказ")
        def add_ingredient_to_order(self, ):
            place_one = self.find_element(ConstructorPageLocators.INGREDIENT_BUN)
            place_two = self.find_element(ConstructorPageLocators.ORDER_CART)
            self.drag_and_drop_element(place_one, place_two)

        def create_an_order(self):
            self.wait_for_visible(ConstructorPageLocators.INGREDIENT_BUN)
            bun_elem = self.find_element(ConstructorPageLocators.INGREDIENT_BUN)
            cart_elem = self.find_element(ConstructorPageLocators.ORDER_CART)
            self.drag_and_drop_element(bun_elem, cart_elem)
            self.wait_for_visible(ConstructorPageLocators.INGREDIENT_SAUCE)
            sauce_elem = self.find_element(ConstructorPageLocators.INGREDIENT_SAUCE)
            self.drag_and_drop_element(sauce_elem, cart_elem)
            self.wait_for_visible(ConstructorPageLocators.INGREDIENT_FILLING)
            filling_elem = self.find_element(ConstructorPageLocators.INGREDIENT_FILLING)
            self.drag_and_drop_element(filling_elem, cart_elem)
            self.wait_for_clickable(ConstructorPageLocators.ORDER_CREATE_BTN)
            self.forse_click(ConstructorPageLocators.ORDER_CREATE_BTN)

            self.wait_for_visible(ConstructorPageLocators.ORDER_MODAL_FRAME)
            self.wait_for_invisible(ConstructorPageLocators.DEFAULT_ORDER_NUMBER)
            self.wait_for_visible(ConstructorPageLocators.ORDER_IS_PREPARING_TEXT)

            order_number = self.get_text_element(ConstructorPageLocators.REAL_ORDER_NUMBER)

            self.forse_click(ConstructorPageLocators.CLOSE_ORDER_MENU_BTN)

            return order_number

        @allure.step("Клик по кнопке 'Оформить заказ'")
        def click_create_order(self):
            self.forse_click(ConstructorPageLocators.ORDER_CREATE_BTN)

        @allure.step("Проверка сообщения 'Ваш заказ начали готовить'")
        def is_order_preparing_message_visible(self):
            return self.is_visible_element(ConstructorPageLocators.ORDER_IS_PREPARING_TEXT)