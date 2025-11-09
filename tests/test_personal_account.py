from page.auth_page import AuthPage
from faker import Faker
from helpers import help_script
import allure

fake = Faker()


class TestPersonalAccount:
    
    @allure.title("Проверка клика по кнопке Личный кабинет")
    @allure.description(
        "Переход по клику на «Личный кабинет»"
    )
    @allure.feature("Личный кабинет")
    def test_go_to_personal_account(self, personal_page_fxt):
        personal_page, email, name, token = personal_page_fxt
        name_input = personal_page.wait_name_input_visible()
        login_input = personal_page.wait_login_input_visible()
        password_input = personal_page.wait_password_input_visible()
        current_url = personal_page.get_current_url()
        assert '/account/profile' in current_url
        assert name_input.is_displayed()
        assert login_input.is_displayed()
        assert password_input.is_displayed()
        help_script.delete_user(email, name, token)

    @allure.title("Проверка перехода в историю заказов")
    @allure.description(
        "Переход в раздел «История заказов»"
    )
    @allure.feature("Личный кабинет")
    def test_go_to_orders_history(self, personal_page_fxt):
        personal_page, email, name, token = personal_page_fxt
        personal_page.wait_orders_history_button()
        personal_page.click_order_history_button()
        current_url = personal_page.get_current_url()
        assert '/account/order-history' in current_url
        help_script.delete_user(email, name, token)

    @allure.title("Проверка выхода из аккаунта")
    @allure.description(
        "выход из аккаунта"
    )
    @allure.feature("Личный кабинет")
    def test_logout(self, driver, personal_page_fxt):
        personal_page, email, name, token = personal_page_fxt
        personal_page.wait_logout_button_clickable()
        personal_page.click_logout()
        auth_page = AuthPage(driver)
        header = auth_page.wait_header_visible()
        email_input = auth_page.wait_email_input_be_clickable()
        assert header.is_displayed()
        assert email_input.is_displayed()
        help_script.delete_user(email, name, token)



