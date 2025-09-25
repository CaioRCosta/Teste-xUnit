from test_case import TestCase
from test_result import TestResult
from test_stub import TestStub
from test_suite import TestSuite



class TestSuiteTest(TestCase):
    """Testes para a classe TestSuite."""

    def test_suite_size(self):
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))
        assert len(suite.tests) == 3

    def test_suite_success_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.run(result)
        assert result.summary() == '1 run, 0 failed, 0 error'

    def test_suite_multiple_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))
        suite.run(result)
        assert result.summary() == '3 run, 1 failed, 1 error'


if __name__ == "__main__":
    result = TestResult()

    tests = [
        'test_suite_size',
        'test_suite_success_run',
        'test_suite_multiple_run'
    ]

    for test_name in tests:
        TestSuiteTest(test_name).run(result)

    print(result.summary())

