# código do framework
class TestCase:

    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self, result=None):
        """Executa o método de teste e coleta resultados, se result for fornecido."""
        if result:
            result.test_started()  # marca início do teste
        self.set_up()
        try:
            test_method = getattr(self, self.test_method_name)
            test_method()  # executa o teste
        except AssertionError:
            if result:
                result.add_failure(self.test_method_name)
        except Exception:
            if result:
                result.add_error(self.test_method_name)
        self.tear_down()

    def set_up(self):
        pass

    def tear_down(self):
        pass


# classe de teste exemplo
class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')


# rodar os testes manualmente
if __name__ == "__main__":
    # Sem coletar resultados
    test = MyTest('test_a')
    test.run()
    test = MyTest('test_b')
    test.run()
    test = MyTest('test_c')
    test.run()

    # Com TestResult
    from test_result import TestResult
    result = TestResult()
    test = MyTest('test_a')
    test.run(result)
    test = MyTest('test_b')
    test.run(result)
    test = MyTest('test_c')
    test.run(result)

    print(result.summary())
