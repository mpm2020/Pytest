from Pages.LoginPage import login
from Pages.FormPage import form

def test_form(chrome_browser):

    browser =chrome_browser
    main_page = login(browser)
    main_page.go_to_site()
    main_page.enter_credentials()
    main_page= form(browser)
    main_page.register_data()
