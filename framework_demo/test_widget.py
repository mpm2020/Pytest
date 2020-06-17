from pytest import mark

# def get_greeting():
#   greeting="Hola Mundo"
#   return greeting

def test_widget_functions_as_expected():
    # assert "Hola Mundo" == get_greeting()
    assert True

#@mark.skip(reason="Test fail here")
@mark.skip(reason="Broken, fixing next sprint")
def test_this_needs_work():
    assert False


#@mark.skip(reason="Test fail here")
@mark.xfail(reason="This feature should have been deprecated")
def test_widget_fails():
    assert False


def some_convenience_function():
    print("I do some extra work")
