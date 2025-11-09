from selenium.webdriver.common.by import By

EMAIL_INPUT = (By.NAME, 'name')
MODAL_CLOSE_BUTTON = (
    By.XPATH,
    "//div[contains(@class,'Modal_modal__') or contains(@class,'Modal_modal')]//button[contains(@class,'close') or contains(@class,'Close')]",
)  # Закрыть на модальном окне с деталями ингредиента, модальном экране успеха, деталях заказа

VIEW_PASSWORD_BUTTON = (By.XPATH, '//div[contains(@class, "input_type_password")]//div[contains(@class, "input__icon-action")]')

