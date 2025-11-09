from selenium.webdriver.common.by import By

ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

NAME_VALUE_INPUT =  (By.XPATH, '//label[normalize-space()="Имя"]/following-sibling::*[self::input or self::span or self::p][1]')
LOGIN_VALUE_INPUT = (By.XPATH,
    '//label[normalize-space()="Логин"]/following-sibling::*[self::input or self::span or self::p][1]'
)
PASSWORD_VALUE_INPUT = (By.XPATH,
    '//label[normalize-space()="Пароль"]/following-sibling::input[@type="password" or @type="text"][1]'
)