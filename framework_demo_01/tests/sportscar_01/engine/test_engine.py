import time
#from selenium import webdriver
from pytest import mark

@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    #browser=webdriver.Chrome()
     #my_browser=chrome_browser
     #my_browser.get('http://www.google.com')
     #time.sleep(5)
     second_browser=chrome_browser
     #second_browser.get('http://www.amazon.com')
     #chrome_browser.get('http://www.artofmanliness.com/articles/how-a-cars-engine-works')
     second_browser.get('http://www.artofmanliness.com/articles/how-a-cars-engine-works')
     assert True
