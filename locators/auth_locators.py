from selenium.webdriver.common.by import By

PASSWORD_RECOVERY_BUTTON = (By.XPATH, '//a[text()="Восстановить пароль"]')

PASSWORD_INPUT = (By.NAME, 'Пароль')
LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')

ENTER_HEADER = (By.XPATH, '//h2[text()="Вход"]')