from src.test_case import TestCase
from src.test_result import TestResult

class TestStub(TestCase):
    def test_success(self):
        assert True

    def test_failure(self):
        assert False

    def test_error(self):
        raise Exception

if __name__ == "__main__":
    result = TestResult()

    TestStub('test_success').run(result)
    TestStub('test_failure').run(result)
    TestStub('test_error').run(result)

    print(result.summary())

