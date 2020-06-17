#from selenium import webdriver
from pytest import mark

# @mark.smoke
# pytest -m smoke
# pytest -m body
# pytest -m "body or engine"
# pytest -m "not entertainment"
# pytest -m "body and door"

@mark.smoke
@mark.body
class BodyTests:
    @mark.ui
    #@mark.body
    def test_can_navigate_to_body_page(self,chrome_browser):
        #browser=webdriver.Chrome()
        chrome_browser.get('http://www.motortrend.com')
        assert True


    #@mark.body
    def test_bumper(self):
        assert True

    #@mark.body
    def test_windshield(self):
        assert True
