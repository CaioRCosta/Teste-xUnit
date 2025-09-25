from test_case import TestCase


class TestSuite:
    """Representa uma coleção de TestCases ou outras TestSuites."""

    def __init__(self):
        self.tests = []

    def add_test(self, test):
        """Adiciona um TestCase ou TestSuite à suíte"""
        self.tests.append(test)

    def run(self, result):
        """Executa todos os testes da suíte"""
        for test in self.tests:
            test.run(result)

