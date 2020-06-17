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
    @mark.door
    #@mark.body
    def test_body_as_expected(self):
        assert True


    #@mark.body
    def test_bumper(self):
        assert True

    #@mark.body
    def test_windshield(self):
        assert True
