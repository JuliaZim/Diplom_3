import allure
from page.base_page import BasePage
from locators import password_recovery_locators
from locators import base_locators


class RecoveryPasswordPage(BasePage):
    @allure.step("Ожидание кликабельности поля Email на странице Восстановить пароль")
    def wait_email_input(self):
        return self.wait_for_element_to_be_clickable(base_locators.EMAIL_INPUT)

    @allure.step("Заполнить поле email")
    def set_email(self, email):
        return self.send_keys_element(base_locators.EMAIL_INPUT, email)

    @allure.step(
        "Ожидание кликабельности кнопки Восстановить на странице Восстановить пароль"
    )
    def wait_recovery_button(self):
        return self.wait_for_element_to_be_clickable(
            password_recovery_locators.RECOVERY_BUTTON
        )

    @allure.step("Клик по кнопке Восстановить")
    def click_recovery_button(self):
        return self.click_element(password_recovery_locators.RECOVERY_BUTTON)

    @allure.step("Ожидание видимости поля Введите код на странице Восстановить пароль")
    def wait_input_for_email_code(self):
        return self.wait_for_element_to_be_visible(
            password_recovery_locators.CODE_INPUT
        )

   # @allure.step("Найти инпут email на странице Восстановить пароль")
    #def find_input_for_email_code(self):
    #    return self.find_element(password_recovery_locators.CODE_INPUT)

    @allure.step("Ожидание кликабельности кнопки видимости пароля")
    def wait_password_view_clickable(self):
        return self.wait_for_element_to_be_clickable(base_locators.VIEW_PASSWORD_BUTTON)

    @allure.step("Клик по кнопке видимости пароля")
    def click_password_view_button(self):
        return self.click_element(base_locators.VIEW_PASSWORD_BUTTON)

    @allure.step("Получить атрибут type у поля Новый пароль")
    def get_attribute_password_view_btn(self):
        return self.find_element(
            password_recovery_locators.NEW_PASSWORD_INPUT
        ).get_attribute("type")

    @allure.step("Заполнить email и нажать Восстановить")
    def fill_email_and_click_recovery(self, email):
        self.wait_email_input()
        self.set_email(email)
        self.wait_recovery_button()
        self.click_recovery_button()
