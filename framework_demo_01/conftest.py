from pytest import fixture
from selenium import webdriver


@fixture(scope='function')
#One browser down here
#@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    #return browser
    yield browser
    print("I am tearing down this browser")
