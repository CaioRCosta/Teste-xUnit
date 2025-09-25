from test_case import TestCase

class TestStub(TestCase):

    def test_success(self):
        assert True  # teste que passa

    def test_failure(self):
        assert False  # teste que falha (AssertionError)

    def test_error(self):
        raise Exception  # teste que lança erro

