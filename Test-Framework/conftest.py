from pytest import fixture
from selenium import webdriver


@fixture(scope='session')
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()