import pytest


@pytest.yield_fixture()
def setup():
    print("Opening URL to SignUp")
    yield
    print ("Closing browser after SignUp")


def test_signupByemail(setup):
    print("this is signup by email test")


def test_signupByfacebook(setup):
    print("this is signup by facebook test")
