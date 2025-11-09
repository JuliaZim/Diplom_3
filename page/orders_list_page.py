import allure
from page.base_page import BasePage
from locators import orders_list_locators


class OrdersListPage(BasePage):
    # Ожидание элементов
    @allure.step('Ожидание видимости заголовка на странице Лента заказов')
    def wait_headers_visible(self):
        return self.wait_for_element_to_be_visible(orders_list_locators.ORDERS_LIST_HEADER)

    @allure.step('Ожидание кликабельности кнопка заказа на странице Лента заказов')
    def wait_order_button_clickable(self):
        self.wait_for_element_to_be_clickable(orders_list_locators.LAST_ORDER_BUTTON)

    @allure.step('ожидание видимости модального окна с деталями заказа на странице Лента заказов')
    def wait_order_details_modal_visible(self):
        return self.wait_for_element_to_be_visible(orders_list_locators.ORDER_DETAILS_MODAL)

    @allure.step('Ожидание видимости каунтера заказов на странице Лента заказов')
    def wait_counter_order_any_time(self,locator):
        return self.wait_for_element_to_be_visible(locator)

    @allure.step('Ожидание видимости заказа в блоке В работе на странице Лента заказов')
    def wait_order_in_work_block(self, order_id):
        by, locator = orders_list_locators.IN_WORK_ORDER_ID
        formatted_locator = (by, locator.format(order_id=order_id))
        return self.wait_for_element_to_be_visible(formatted_locator)

    @allure.step('Ожидание видимости заказа в списке заказов на странице Лента заказов')
    def wait_user_order_in_list(self, order_id):
        by, locator = orders_list_locators.USER_ORDER_ID
        formatted_locator = (by, locator.format(order_id=order_id))
        return self.wait_for_element_to_be_visible(formatted_locator)
    
    # клик в элементы
    @allure.step('Клик по заказу на странице Лента заказов')
    def click_order_button(self):
        self.click_element(orders_list_locators.LAST_ORDER_BUTTON)

    