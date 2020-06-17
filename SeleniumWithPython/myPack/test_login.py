import pytest


@pytest.yield_fixture()
def setup():
    print("Opening URL to Login")
    yield
    print ("Closing browser after login")


def test_loginByemail(setup):
    print("this is login by email test")


def test_loginByfacebook(setup):
    print("this is login by facebook test")
