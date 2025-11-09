from selenium.webdriver.common.by import By

LAST_ORDER_BUTTON = (By.XPATH, "//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']/li[last()]/a")
LAST_ORDER_ID = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6'][last()]/a/div/p[1]")