from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class BasePage:

    OVERLAY = (By.CSS_SELECTOR, '.Modal_modal_overlay__x2ZCr')

    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 7)


    # Общие действия с элементами
    def wait_for_element_to_be_clickable(self, locator):
        self.wait_overlay_gone()
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_visible(self, locator):
        #self.wait_overlay_gone()
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click_element(self, locator):
        #self.wait_overlay_gone()
        el = self.wait_for_element_to_be_clickable(locator)
        try:
            el.click()
        except ElementClickInterceptedException:
            # На всякий – ещё раз ждём и кликаем JS'ом как запасной вариант (особенно для Firefox)
            self.wait_overlay_gone()
            self.driver.execute_script("arguments[0].click();", el)
        
    
    def send_keys_element(self, locator, value):
        self.wait_overlay_gone()
        return self.find_element(locator).send_keys(value)
    
    def get_text_from_element(self, locator):
        return self.find_element(locator).text
    
    def scroll_to_element(self, locator):
        self.wait_overlay_gone()
        return self.driver.execute_script("arguments[0].scrollIntoView();", (locator))
    
    def execute_js_script(self, script, src, dst):
        self.wait_overlay_gone()
        return self.driver.execute_script(script, src, dst)
        
    def get_current_url(self):
        return self.driver.current_url
    
    def wait_overlay_gone(self):
        try:
            self.wait.until(
                EC.invisibility_of_element_located(self.OVERLAY) 
            )
        except TimeoutException:
            # Ничего: если оверлей всё ещё есть – кликовая обёртка ещё раз попробует
            pass

    def refresh(self):
        self.driver.refresh()