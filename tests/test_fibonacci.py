import builtins
from unittest import mock
from Modulo2.fibonacci import Fibonacci


class TestFibonacci:
    def test_sequencia_fibonacci(self):
        with mock.patch.object(builtins,'input',lambda _ : 5):
            sequencia = Fibonacci.sequencia_fibonacci()
            assert len(sequencia) == 5
        
