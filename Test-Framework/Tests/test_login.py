from Pages.LoginPage import login

def test_login(chrome_browser):

    browser =chrome_browser
    main_page = login(browser)
    main_page.go_to_site()
    main_page.enter_credentials()
    assert browser.title == "AUT Form – TestFaceClub"
