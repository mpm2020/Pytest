#from selenium import webdriver
from pytest import mark

@mark.ui
@mark.entertainment
def test_can_navigate_to_entertainment_page(chrome_browser):
    # browser=webdriver.Chrome()
    chrome_browser.get('http://www.siriusxm.com')
    assert True

