from selenium import webdriver

APP_DIR = os.path.dirname(os.path.dirname("__filename__"))


def test_chrome():
    _chrome_driver = os.path.join(APP_DIR, 'chromedriver')

    _chrome_options = webdriver.ChromeOptions()
    _chrome_options.add_argument('--headless')
    _chrome_options.add_argument('--no-sandbox')
    _chrome_options.add_argument('--disable-dev-shm-usage')
    _chrome_options.add_argument('--disable-gpu')

    _driver = webdriver.Chrome(self._chrome_driver, chrome_options=self._chrome_options)
    _driver.implicitly_wait(3)

    _driver.quit()
