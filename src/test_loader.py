from test_suite import TestSuite
from test_case import TestCase

class TestLoader:
    TEST_METHOD_PREFIX = 'test'

    def get_test_case_names(self, test_case_class):
        methods = dir(test_case_class)
        test_method_names = list(filter(lambda m: m.startswith(self.TEST_METHOD_PREFIX), methods))
        return test_method_names

    def make_suite(self, test_case_class):
        suite = TestSuite()
        for name in self.get_test_case_names(test_case_class):
            suite.add_test(test_case_class(name))
        return suite

