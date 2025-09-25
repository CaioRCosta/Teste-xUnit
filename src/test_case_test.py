from test_case import TestCase
from test_result import TestResult
from test_stub import TestStub
from test_suite import TestSuite

class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert test.log == "setUp test_method tearDown "

    def test_result(self):
        test = WasRun("test_method")
        test.run(self.result)
        self.assert_equal(self.result.summary(), "1 run, 0 failed, 0 error")

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        test.run(self.result)
        self.assert_equal(self.result.summary(), "1 run, 1 failed, 0 error")

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        self.assert_equal(self.result.summary(), "1 run, 1 failed, 0 error")

    def test_error_result(self):
        test = WasRun("test_error_method")
        test.run(self.result)
        self.assert_equal(self.result.summary(), "1 run, 0 failed, 1 error")

    def test_suite(self):
        suite = TestSuite()
        suite.add_test(WasRun("test_method"))
        suite.add_test(WasRun("test_broken_method"))
        suite.run(self.result)
        self.assert_equal(self.result.summary(), "2 run, 1 failed, 0 error")

    def test_suite_with_error(self):
        suite = TestSuite()
        suite.add_test(WasRun("test_error_method"))
        suite.run(self.result)
        self.assert_equal(self.result.summary(), "1 run, 0 failed, 1 error")


    def test_assert_true(self):
        self.assert_true(True)

    def test_assert_false(self):
        self.assert_false(False)

    def test_assert_equal(self):
        self.assert_equal("", "")
        self.assert_equal("foo", "foo")
        self.assert_equal([], [])
        self.assert_equal(['foo'], ['foo'])
        self.assert_equal((), ())
        self.assert_equal(('foo',), ('foo',))
        self.assert_equal({}, {})
        self.assert_equal({'foo'}, {'foo'})

    def test_assert_in(self):
        animals = {'monkey': 'banana', 'cow': 'grass', 'seal': 'fish'}
        self.assert_in('a', 'abc')
        self.assert_in('foo', ['foo'])
        self.assert_in(1, [1, 2, 3])
        self.assert_in('monkey', animals)


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.log = ""

    def setUp(self):
        self.log = "setUp "

    def test_method(self):
        self.log += "test_method "

    def test_broken_method(self):
        raise Exception

    def test_error_method(self):
        1 / 0

    def tearDown(self):
        self.log += "tearDown "
        
class TestSpy(TestCase):
    def setUp(self):
        self.was_set_up = False
        self.was_run = False
        self.was_tear_down = False
        self.log = ""

    def test_method(self):
        self.was_run = True
        self.log += "test_method "

    def setUp(self):
        self.was_set_up = True
        self.log = "set_up "

    def tearDown(self):
        self.was_tear_down = True
        self.log += "tear_down"

