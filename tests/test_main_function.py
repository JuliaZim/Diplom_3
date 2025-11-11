from page.main_page import MainPage
from page.orders_list_page import OrdersListPage
from faker import Faker
from helpers import help_script
import allure

fake = Faker()


class TestMainFunction:
    @allure.title("Проверка клика на кнопку Конструктор")
    @allure.description(
        "Создаем клиента, логинимся, заходим на страницу Личный кабинет, кликаем на кнопку конструктор, ожидаем перехода на страницу сбора заказа. Удаляем юзера"
    )
    @allure.feature("Основной функционал")
    def test_click_constuctor_button(self, driver, personal_page_fxt):
        personal_page, email, name, token = personal_page_fxt
        main_page = MainPage(driver)
        main_page.wait_constructor_button()
        main_page.click_constructor_button()
        header = main_page.wait_header_visible()
        assert header.is_displayed()


    @allure.title("Проверка клика на кнопку Лента Заказов")
    @allure.description(
        "Создаем клиента, логинимся, заходим на главную, кликаем на кнопку Лента заказов, ожидаем перехода на страницу с заказами. Удаляем юзера"
    )
    @allure.feature("Основной функционал")
    def test_click_orders_list_button(self, driver, main_page):
        main_page, email, name, token = main_page
        main_page.wait_orders_list_button()
        main_page.click_orders_list_button()
        orders_list = OrdersListPage(driver)
        current_url = orders_list.get_current_url()
        header = orders_list.wait_headers_visible()
        assert '/feed' in current_url
        assert header.is_displayed()

    @allure.title("Проверка клика на ингредиент")
    @allure.description(
        "Создаем клиента, логинимся, заходим на главную, если кликнуть на ингредиент, появится всплывающее окно с деталями. Удаляем юзера"
    )
    @allure.feature("Основной функционал")
    def test_click_to_ingredient(self, main_page):
        main_page, email, name, token = main_page
        main_page.wait_ingredient_button()
        main_page.click_ingredient_button()
        modal = main_page.wait_ingredient_modal_visible()
        assert modal.is_displayed()


    @allure.title("Проверка закрытия модального окна с деталями ингредиета")
    @allure.description(
        "Создаем клиента, логинимся, заходим на главную, если кликнуть на ингредиент, появится всплывающее окно с деталями. Всплывающее окно закрывается кликом по крестику. Удаляем юзера"
    )
    @allure.feature("Основной функционал")
    def test_close_detials_ingredient_modal(self, main_page):
        main_page, email, name, token = main_page
        main_page.wait_ingredient_button()
        main_page.click_ingredient_button()
        main_page.click_close_modal_button()
        modal = main_page.wait_ingredient_modal_invisible()
        assert not modal.is_displayed()

    
    @allure.title("Проверка каунтера ингредиента")
    @allure.description(
        "Создаем клиента, логинимся, при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента. Удаляем юзера"
    )
    @allure.feature("Основной функционал")
    def test_increase_counter(self, main_page):
        main_page, email, name, token = main_page
        main_page.wait_ingredient_button()       
        counter_value_0 = main_page.find_counter().text
        main_page.drag_first_bun_to_constructor()
        counter_value_1 = main_page.find_counter().text
        assert int(counter_value_1) ==  int(counter_value_0) + 2
        
    @allure.title("Проверка создания заказа")
    @allure.description(
        "Создаем клиента, логинимся, залогиненный пользователь может оформить заказ. Удаляем юзера"
    )
    @allure.feature("Основной функционал")
    def test_place_order_login_user(self, main_page):
        main_page, email, name, token = main_page
        main_page.wait_ingredient_button()   
        main_page.create_burger_for_order()
        main_page.wait_create_order_button_clickable()
        main_page.click_create_order_button()
        modal = main_page.wait_succes_order_modal()
        assert modal.is_displayed()
