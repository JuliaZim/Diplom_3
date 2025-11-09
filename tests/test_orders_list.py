
from page.personal_account_page import PersonalAccountPage
from page.orders_list_page import OrdersListPage
from faker import Faker
from helpers import help_script
import pytest
from locators import orders_list_locators
import allure

fake = Faker()


class TestOrdersList:
            
    @allure.title("Проверка клика по заказу")
    @allure.description(
        "Создаем клиента, логинимся, если кликнуть на заказ на странице Лента заказов, откроется всплывающее окно с деталями. Удаляем юзера"
    )
    @allure.feature("Лента заказов")
    def test_click_to_order(self, driver, main_page):
        main_page, email, name, token = main_page
        main_page.wait_orders_list_button()
        main_page.click_orders_list_button()
        orders_list_page = OrdersListPage(driver)
        orders_list_page.wait_order_button_clickable()
        orders_list_page.click_order_button()
        modal = orders_list_page.wait_order_details_modal_visible()
        assert modal.is_displayed()
        help_script.delete_user(email, name, token)

            
    @allure.title("Проверка отображения заказа пользователя в ленте заказов")
    @allure.description(
        "Создаем клиента, логинимся, создаем заказ. Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов». Удаляем юзера"
    )
    @allure.feature("Лента заказов")
    def test_user_order_in_orders_list(self, driver, main_page):
        main_page, email, name, token = main_page
        main_page.create_order()
        main_page.click_personal_account_button()
        personal_page = PersonalAccountPage(driver)
        order_id = personal_page.go_to_personal_page_and_get_order_id()
        main_page.click_orders_list_button()
        order_list_page = OrdersListPage(driver)
        order = order_list_page.wait_user_order_in_list(order_id)
        assert order.is_displayed()
        help_script.delete_user(email, name, token)
    
          
    @allure.description(
        "Создаем клиента, логинимся, создаем заказ. При создании нового заказа счётчик Выполнено за всё время и Выполнено за сегодня увеличивается,. Удаляем юзера"
    )
    @allure.feature("Лента заказов")
    @pytest.mark.parametrize('params', [(orders_list_locators.DONE_ALL_TIME_NUMBER, 'Увеличение счетчика заказов За всё время'), (orders_list_locators.DONE_TODAY_NUMBER, 'Увеличение счетчика заказов За сегодня')])
    def test_increase_counter_order_all_time(self, driver, main_page, params):
        param, test_title = params
        allure.dynamic.title(test_title)
        main_page, email, name, token = main_page
        main_page.click_orders_list_button()
        order_list_page = OrdersListPage(driver)
        order_list_page.wait_headers_visible()
        count_0 = int(order_list_page.wait_counter_order_any_time(param).text)
        main_page.click_constructor_button()
        main_page.create_order()
        main_page.click_orders_list_button()
        order_list_page.wait_headers_visible()
        order_list_page.refresh()
        count_1 = int(order_list_page.wait_counter_order_any_time(param).text)
        assert count_1 > count_0
        help_script.delete_user(email, name, token)


    @allure.title("Вновь созданнй заказ опадает в блок В рботе")
    @allure.description(
        "Создаем клиента, логинимся, создаем заказ. после оформления заказа его номер появляется в разделе В работе. Удаляем юзера"
    )
    @allure.feature("Лента заказов")
    def test_order_number_in_work_block(self, driver, main_page):
        main_page, email, name, token = main_page
        order_id_in_modal = main_page.create_order().text
        main_page.click_orders_list_button()
        order_list_page = OrdersListPage(driver)
        order_list_page.wait_headers_visible()
        order_id_in_block = order_list_page.wait_order_in_work_block(order_id_in_modal).text
        assert f'{order_id_in_block}' == f'0{order_id_in_modal}'
        help_script.delete_user(email, name, token)




    