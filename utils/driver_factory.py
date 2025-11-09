from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class WebDriverFactory:
    @staticmethod
    def create_browser(browser_name, headless = False):
        name = browser_name.lower()
        if name == "chrome":
            options = ChromeOptions()
            if headless:
                # Можно добавить опции для Chrome, если нужно
                options.add_argument("--headless=new") 
            return webdriver.Chrome(options=options)
        elif name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
                # Можно добавить опции для Firefox, если нужно
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
