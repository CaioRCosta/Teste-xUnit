# run_all.py
from test_case_test import TestCaseTest, TestSpy
from test_suite_test import TestSuiteTest
from test_loader_test import TestLoaderTest
from test_loader import TestLoader
from test_runner import TestRunner
from test_suite import TestSuite

# --- Criar suites usando TestLoader ---
loader = TestLoader()

test_case_suite = loader.make_suite(TestCaseTest)
test_suite_suite = loader.make_suite(TestSuiteTest)
test_loader_suite = loader.make_suite(TestLoaderTest)

# --- Suíte principal que agrupa todas ---
all_tests_suite = TestSuite()
all_tests_suite.add_test(test_case_suite)
all_tests_suite.add_test(test_suite_suite)
all_tests_suite.add_test(test_loader_suite)

# --- Executar todos os testes ---
runner = TestRunner()
runner.run(all_tests_suite)

