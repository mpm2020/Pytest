from example import Hi, Bye, How_are_you
import pytest


@pytest.fixture
def bob():
    return {"name": "Bob"}


def test_hello(bob):
    assert Hi(bob) == 'Hi Bob'


def test_Bye(bob):
    assert Bye(bob) == 'Bye Bob'


def test_How_are_you(bob):
    assert How_are_you(bob) == 'How are you Bob'
