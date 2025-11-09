from selenium.webdriver.common.by import By

#PSW_RECOVERY_HEADER = (By.XPATH, '//h2[normalize-space()="Восстановление пароля"]')
RECOVERY_BUTTON     = (By.XPATH, "//button[normalize-space()='Восстановить']")
CODE_INPUT          = (By.XPATH, "//label[normalize-space()='Введите код из письма']/following-sibling::input")
NEW_PASSWORD_INPUT  = (By.NAME, 'Введите новый пароль')