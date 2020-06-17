def greet(name):
    return "Hello " + name


def test_greet():
    assert greet('Mariana') == "Hello Mariana"
