import pytest
from complex import Complex
from complex import IsFloatOrInt

class TestComplex():

    def test_add(self):
        testsuite = [
            (Complex(1, 2), Complex(0, 1), "13i"),
            (Complex(0, 2), Complex(0, 0), "02i"),
            (Complex(0, 0), Complex(0, 1), "01i"),
        ]
        for test in testsuite:
            answer = "{real}{imaginary}i".format(real=test[0].__add__(test[1]).real, imaginary=test[0].__add__(test[1]).imaginary)
            assert answer == test[2]

    def test_sub(self):
        testsuite = [
            (Complex(1, 2), Complex(0, 1), "11i"),
            (Complex(1, 1), Complex(2, 2), "-1-1i"),
            (Complex(-1, -1), Complex(-2, 2), "1-3i"),
        ]
        for test in testsuite:
            answer = "{real}{imaginary}i".format(real=test[0].__sub__(test[1]).real, imaginary=test[0].__sub__(test[1]).imaginary)
            assert answer == test[2]

    def test_mul(self):
        testsuite = [
            (Complex(2, 3), Complex(1, 1), "-15i"),
            (Complex(2, 3), 4, "8-12i"),
            (Complex(7, 8), 9, "63-72i"),
        ]
        for test in testsuite:
            mul =  test[0].__mul__(test[1])
            answer = "{real}{imaginary}i".format(real=mul.real, imaginary=mul.imaginary)
            assert answer == test[2]

    def test_IsFloatOrInt(self):
        testsuite = [
            (10, True),
            (-1, True),
            (1.1, True),
            (Complex(1, 2), False)
        ]
        for test in testsuite:
            answer = IsFloatOrInt(test[0])
            assert answer == test[1]

        