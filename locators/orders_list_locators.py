from selenium.webdriver.common.by import By

ORDERS_LIST_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
#ORDER_LIST = (By.CLASS_NAME, 'OrderFeed_list__OLh59')

#DONE_HEADER = (By.XPATH, '//div[@class="OrderFeed_orderStatusBox__1d4q2 mb-15"]/p[1]')
#IN_WORK_HEADER = (By.XPATH, '//div[@class="OrderFeed_orderStatusBox__1d4q2 mb-15"]/p[2]')
IN_WORK_ORDER_ID = (By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[contains(normalize-space(.), "{order_id}")]')

#DONE_ALL_TIME_HEADER = (By.XPATH, "//p[text()='Выполнено за все время:']")
DONE_ALL_TIME_NUMBER = (By.XPATH, "//div[@class='OrderFeed_ordersData__1L6Iv']/div[2]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][1]")

#DONE_TODAY_HEADER = (By.XPATH, "//p[text()='Выполнено за сегодня:']")
DONE_TODAY_NUMBER = (By.XPATH, "//div[@class='OrderFeed_ordersData__1L6Iv']/div[3]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][1]")

LAST_ORDER_BUTTON = (By.XPATH,  '//ul[@class="OrderFeed_list__OLh59"]/li[1]/a')
ORDER_DETAILS_MODAL = (By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]')

#ID_LAST_ORDER_IN_LIST = (By.CSS_SELECTOR, 'li.OrderHistory_listItem__2x95r:nth-child(1) > a:nth-child(1) > div:nth-child(1) > p:nth-child(1)')
#ID_LAST_ORDER_IN_MODAL = (By.XPATH, '//div[@class = "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]/p[1]')
#NAME_ORDER_IN_MODAL = (By.XPATH, '//div[@class = "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]/h2')
#STATUS_ORDER_IN_MODAL = (By.XPATH, '//div[@class = "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]/p[2]')
#CONTENT_ORDER_HEADER_IN_MODAL = (By.XPATH, '//div[@class = "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]/p[2]')
#CONTENT_ORDER_IN_MODAL = (By.CLASS_NAME, 'Modal_list__2sHWc')
#PRICE_ORDER_IN_MODAL = (By.XPATH, '//div[@class = "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]/div/div/p')

USER_ORDER_ID = (By.XPATH, "//p[contains(text(), '{order_id}')]/parent::div/parent::a")
