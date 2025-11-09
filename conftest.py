import pytest
from data import urls
from utils.driver_factory import WebDriverFactory
from helpers import help_script
from page.auth_page import AuthPage
from page.main_page import MainPage
from page.personal_account_page import PersonalAccountPage
import allure

# Фикстура
@allure.step("Запуск браузера")
@pytest.fixture(scope='function', params=['chrome','firefox'])
def driver(request):
    driver = WebDriverFactory.create_browser(request.param)
    driver.get(urls.main_page_burger_url)
    yield driver
    driver.quit()  

@allure.step("Переход на главную страницу")
@pytest.fixture(scope='function')
def main_page(driver):
        email, password, name, token = help_script.create_user()
        auth_page = AuthPage(driver)
        auth_page.login(email, password)
        main_page = MainPage(driver)
        return main_page, email, name, token

@allure.step("перенход на страницу Личный кабинет")
@pytest.fixture(scope='function')
def personal_page_fxt(driver, main_page):
        main_page, email, name, token = main_page
        main_page.wait_personal_account_button()
        main_page.click_personal_account_button()
        personal_page = PersonalAccountPage(driver)
        return personal_page, email, name, token
