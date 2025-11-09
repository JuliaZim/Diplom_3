from page.auth_page import AuthPage
from page.recovery_psw_page import RecoveryPasswordPage
import pytest
from faker import Faker
import allure


fake = Faker()


class TestRecoveryButton:
    @allure.title("Проверка перехода по кнопке Восстановить пароль")
    @allure.description(
        "Переход на страницу восстановления пароля по кнопке «Восстановить пароль»"
    )
    @allure.feature("Восстановление пароля")
    def test_click_recovery_psw_btn(self, driver):
        auth_page = AuthPage(driver)
        auth_page.go_to_recovery_password_page()
        recovery_page = RecoveryPasswordPage(driver)
        email_el = recovery_page.wait_email_input()
        recovery_button_el = recovery_page.wait_recovery_button()
        assert email_el.is_displayed() and recovery_button_el.is_displayed()

    @allure.title("Проверка заполнения блока email при восстановлении пароля")
    @allure.description(
        "Переход на страницу восстановления пароля по кнопке «Восстановить пароль», ввод почты и клик по кнопке «Восстановить»"
    )
    @allure.feature("Восстановление пароля")
    @pytest.mark.parametrize("email", [fake.email()])
    def test_go_to_psw_recovery(self, driver, email):
        auth_page = AuthPage(driver)
        auth_page.go_to_recovery_password_page()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.fill_email_and_click_recovery(email)
        element = recovery_page.wait_input_for_email_code()
        assert element.is_displayed() == True

    @allure.title("Проверка показа пароля")
    @allure.description(
        "Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его."
    )
    @allure.feature("Восстановление пароля")
    @pytest.mark.parametrize("email", [fake.email()])
    def test_click_password_view_btn(self, driver, email):
        auth_page = AuthPage(driver)
        auth_page.go_to_recovery_password_page()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.fill_email_and_click_recovery(email)
        recovery_page.wait_password_view_clickable()
        old_value = recovery_page.get_attribute_password_view_btn()
        recovery_page.click_password_view_button()
        new_value = recovery_page.get_attribute_password_view_btn()
        assert old_value == 'password' and new_value == 'text'