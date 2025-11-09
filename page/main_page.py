import allure
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage
from locators import base_locators, main_page_locators
from helpers import help_script


class MainPage(BasePage):
    # методы ожидания элементов

    @allure.step('Ожидание кликабельности кнопки Личный кабинет')
    def wait_personal_account_button(self):
        self.wait_for_element_to_be_clickable(
            main_page_locators.PERSONAL_ACCOUNT_BUTTON
        )
    @allure.step('Ожидание кликабельности кнопки Конструктор')
    def wait_constructor_button(self):
        self.wait_for_element_to_be_clickable(
            main_page_locators.CONSTRUCTOR_BUTTON
        )

    @allure.step('Ожидание кликабельности кнопки Лист заказов')
    def wait_orders_list_button(self):
        self.wait_for_element_to_be_clickable(
            main_page_locators.ORDERS_LIST_BUTTON
        )

    @allure.step('Ожидание видимости заголовка Соберите бургер')
    def wait_header_visible(self):
        return self.wait_for_element_to_be_visible(main_page_locators.HEADER)
    
    @allure.step('Ожидание кликабельности кнопки ингредиента')
    def wait_ingredient_button(self):
        self.wait_for_element_to_be_clickable(main_page_locators.FIRST_BUN_BUTTON)

    @allure.step('Ожидание видимости модального окна с деталями заказа')
    def wait_ingredient_modal_visible(self):
        return self.wait_for_element_to_be_visible(main_page_locators.INGREDIENT_MODAL)
    
    allure.step('Ожидание невидимости модального окна с деталями заказа')
    def wait_ingredient_modal_invisible(self):
        return self.wait.until(EC.invisibility_of_element_located(main_page_locators.INGREDIENT_MODAL))
    
    @allure.step('Ожидание кликабельности кнопки Оформить заказ')
    def wait_create_order_button_clickable(self):
        self.wait_for_element_to_be_clickable(main_page_locators.CREATE_ORDER_BUTTON)

    @allure.step('Ожидание видимости модального окна успеха заказа')
    def wait_succes_order_modal(self):
        return self.wait_for_element_to_be_visible(main_page_locators.SUCCESS_ORDER_MODAL)

    @allure.step('Ожидание видимости order_id заказа')
    def wait_succes_order_modal_order_id(self):
        return self.wait_for_element_to_be_visible(main_page_locators.ORDER_ID)


    # методы кликнуть на элемент    
    @allure.step('Клик на кнопку Личный кабинет')
    def click_personal_account_button(self):
        self.click_element(main_page_locators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку Конструктор')
    def click_constructor_button(self):
        self.click_element(main_page_locators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на кнопку Лист заказов')
    def click_orders_list_button(self):
        self.click_element(main_page_locators.ORDERS_LIST_BUTTON)

    @allure.step('Клик на кнопку ингредиента')
    def click_ingredient_button(self):
        self.click_element(main_page_locators.FIRST_BUN_BUTTON)

    @allure.step('Клик на кнопку закрыть модальное окно')
    def click_close_modal_button(self):
        self.click_element(base_locators.MODAL_CLOSE_BUTTON)

    @allure.step('Клик на кнопку Оформить заказ')
    def click_create_order_button(self):
        self.click_element(main_page_locators.CREATE_ORDER_BUTTON)

    # DND
    @allure.step('Перетащить элемент')
    def drag_html5(self, source_locator, target_locator):
        src = self.wait.until(EC.element_to_be_clickable(source_locator))
        dst = self.wait.until(EC.presence_of_element_located(target_locator))
        # На всякий случай скроллим элементы в видимую область
        self.scroll_to_element(src)
        self.scroll_to_element(dst)

        # Само перетаскивание через JS
        self.execute_js_script(help_script.DND_JS, src, dst)

    @allure.step('Перетащить булку в заказ')
    def drag_first_bun_to_constructor(self):
        self.drag_html5(main_page_locators.FIRST_BUN_BUTTON, main_page_locators.CONSTRUCTOR_DROPZONE)

    @allure.step('Перетащить начинку в заказ')
    def drag_first_filling_to_constructor(self):
        self.drag_html5(main_page_locators.FIRST_FILLING_BUTTON, main_page_locators.CONSTRUCTOR_DROPZONE)

    @allure.step('Перетащить соус в заказ')
    def drag_first_sauce_to_constructor(self):
        self.drag_html5(main_page_locators.FIRST_SAUCE_BUTTON, main_page_locators.CONSTRUCTOR_DROPZONE)

    # найти элемент
    @allure.step('Найти каунтер булки')
    def find_counter(self):
        return self.find_element(main_page_locators.FIRST_BUN_COUNTER)
    
    # Функция сбора бургера для заказа
    @allure.step('Собрать бургер для заказа')
    def create_burger_for_order(self):
        self.drag_first_bun_to_constructor()
        self.drag_first_filling_to_constructor()
        self.drag_first_sauce_to_constructor()

    # Функция оформления заказа
    @allure.step('Оформить заказ')
    def create_order(self):
        self.create_burger_for_order()
        self.wait_create_order_button_clickable()
        self.click_create_order_button()
        self.wait_succes_order_modal()
        order_id = self.wait_succes_order_modal_order_id()
        self.click_close_modal_button()
        return order_id
        