import pytest
import test


class TestMathMethods():

    def testaddReturnFour(self):
        shouldBeFour = test.add(2, 2)
        answer = 4
        assert shouldBeFour == answer


    def testReturnWrongEqual(self):
        four = test.add(2, 2)
        answer = 5
        assert four != answer

    def testMultiplyCorrectAnswer(self):
        m = test.multiply(2, 2)
        assert m == 4

    def testMultiplyIncorrectAnswer(self):
        m = test.multiply(2, 2)
        assert m != 5

    def testPowerCorrect(self):
        p = test.power(2, 8)
        assert p == 256

    def testPowerInCorrect(self):
        p = test.power(2, 7)
        assert p != 256




