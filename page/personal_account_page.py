import allure
from page.base_page import BasePage
from locators import (
    personal_account_locators,
    orders_history_locators
)


class PersonalAccountPage(BasePage):
    @allure.step('Ожидание видимости имени на странице Личный кабинет')
    def wait_name_input_visible(self):
        return self.wait_for_element_to_be_visible(
            personal_account_locators.NAME_VALUE_INPUT
        )

    @allure.step('Ожидание видимости логина на странице Личный кабинет')
    def wait_login_input_visible(self):
        return self.wait_for_element_to_be_visible(
            personal_account_locators.LOGIN_VALUE_INPUT
        )

    @allure.step('Ожидание видимости пароля на странице Личный кабинет')
    def wait_password_input_visible(self):
        return self.wait_for_element_to_be_visible(
            personal_account_locators.PASSWORD_VALUE_INPUT
        )

    @allure.step('Ожидание кликабельности кнопки История заказов на странице Личный кабинет')
    def wait_orders_history_button(self):
        return self.wait_for_element_to_be_clickable(
            personal_account_locators.ORDER_HISTORY_BUTTON
        )

    @allure.step('клик по кнопке История заказов')
    def click_order_history_button(self):
        return self.click_element(personal_account_locators.ORDER_HISTORY_BUTTON)

    @allure.step('Ожидание кликабельности кнопки Выход на странице Личный кабинет')
    def wait_logout_button_clickable(self):
        return self.wait_for_element_to_be_clickable(
            personal_account_locators.LOGOUT_BUTTON
        )

    @allure.step('Клик по кнопке Выйти на странице Личный кабинет')
    def click_logout(self):
        return self.click_element(personal_account_locators.LOGOUT_BUTTON)

    @allure.step('Ожидание видимости айди заказа на странице История заказов')
    def get_order_id(self):
        return self.wait_for_element_to_be_visible(orders_history_locators.LAST_ORDER_ID)
    
    @allure.step('Перейти в личный кабинет, История заказов и вернуть айди заказа')
    def go_to_personal_page_and_get_order_id(self):
        self.wait_orders_history_button()
        self.click_order_history_button()
        return self.get_order_id().text