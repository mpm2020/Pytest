from pytest import mark
@mark.smoke
@mark.engine
def test_engine_as_expected():
    assert True
