import allure
from page.base_page import BasePage
from locators import auth_locators
from locators import base_locators

class AuthPage(BasePage):
    @allure.step('Ожидание отображения заголовка')
    def wait_header_visible(self):
        return self.wait_for_element_to_be_visible(auth_locators.ENTER_HEADER) 
    
    @allure.step('Ожидание кнопки "Восстановить пароль"')
    def wait_recovery_button(self):
        self.wait_for_element_to_be_clickable(auth_locators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_recovery_button(self):
        self.click_element(auth_locators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Переход на страницу Восстановить пароль')
    def go_to_recovery_password_page(self):
        self.wait_recovery_button()
        self.click_recovery_button()

    @allure.step('Ожидание кликабельности инпута email')
    def wait_email_input_be_clickable(self):
        return self.wait_for_element_to_be_clickable(base_locators.EMAIL_INPUT)

    @allure.step('Заполнить поле email')
    def fill_email_input(self, email):
        self.send_keys_element(base_locators.EMAIL_INPUT, email)

    @allure.step('Заполнить поле пароль')
    def fill_password_input(self, password):
        self.send_keys_element(auth_locators.PASSWORD_INPUT, password)

    @allure.step('Клик по кнопке Войти')
    def click_login_button(self):
        self.click_element(auth_locators.LOGIN_BUTTON)

    @allure.step('Войти в аккаунт')
    def login(self, email, password):
        self.wait_email_input_be_clickable()
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.click_login_button()

