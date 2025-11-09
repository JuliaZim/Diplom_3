from selenium.webdriver.common.by import By

# Кнопки на верхней панели
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')
CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')
ORDERS_LIST_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')

# Заголовок Соберите бургер
HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")

# Локаторый первых ингредиентов в каждой секции и их каунтеры
# BUN_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
FIRST_BUN_BUTTON = (
    By.XPATH,
    "//h2[text()='Булки']/following::ul[1]/a[1]",
)
FIRST_BUN_COUNTER = (By.XPATH, "//h2[text()='Булки']/following::ul[1]/a[1]/div[1]/p")


FIRST_SAUCE_BUTTON = (
    By.XPATH,
    '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][2]/a[1]',
)


FIRST_FILLING_BUTTON = (
    By.XPATH,
    '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][3]/a[1]',
)


# Кнопка Оформить заказ
CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

# Модальное окно успешного заказа
SUCCESS_ORDER_MODAL = (
    By.XPATH,
    '//p[text()="Ваш заказ начали готовить"]/ancestor::div[3]',
)
ORDER_ID = (
    By.XPATH,
    "//*[contains(@class,'Modal_modal__title__') and contains(@class,'text_type_digits-large')]",
)

# Модельное окно деталей ингредиентов
INGREDIENT_MODAL = (
    By.XPATH,
    "//div[contains(@class,'Modal_modal__') and .//h2[text()='Детали ингредиента']]",
)

# Дропзона конструктора: для перетаскивания ингредиентов
CONSTRUCTOR_DROPZONE = (
    By.XPATH,
    "//ul[@class='BurgerConstructor_basket__list__l9dp_']",
)
