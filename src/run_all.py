from test_loader import TestLoader
from test_runner import TestRunner
from test_case_test import TestCaseTestWithSpy
from test_suite_test import TestSuiteTest
from test_loader_test import TestLoaderTest
from test_suite import TestSuite

loader = TestLoader()

# cria suítes
case_suite = loader.make_suite(TestCaseTestWithSpy)   # contém 8 testes
suite_suite = loader.make_suite(TestSuiteTest)        # contém 3 testes
loader_suite = loader.make_suite(TestLoaderTest)      # contém 4 testes

master = TestSuite()
master.add_test(case_suite)
master.add_test(suite_suite)
master.add_test(loader_suite)

runner = TestRunner()
runner.run(master)  # deve imprimir: 15 run, 0 failed, 0 error

