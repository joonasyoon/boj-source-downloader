from bs4 import BeautifulSoup
from util import Chrome, get_text


def get_driver():
    args = [
        '--headless', '--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu'
    ]
    driver = Chrome().get_driver(arguments=args)
    driver.implicitly_wait(3)
    return driver


def connect(driver):
    driver.get('https://github.com/')
    return driver


# for pytest
def test_main():
    driver = get_driver()
    assert driver is not None

    html = connect(driver).page_source
    soup = BeautifulSoup(html, 'html.parser')
    assert soup is not None

    driver.quit()
