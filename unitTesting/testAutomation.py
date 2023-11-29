import unittest
import test


class TestMathMethods(unittest.TestCase):

    def testaddReturnFour(self):
        shouldBeFour = test.add(2, 2)
        answer = 4
        self.assertEqual(shouldBeFour, answer)

    def testReturnWrongEqual(self):
        four = test.add(2, 2)
        answer = 5
        self.assertNotEqual(four, answer)

    def testMultiplyCorrectAnswer(self):
        m = test.multiply(2, 2)
        self.assertEqual(m, 4)

    def testMultiplyIncorrectAnswer(self):
        m = test.multiply(2, 2)
        self.assertNotEqual(m, 5)

    def testPowerCorrect(self):
        p = test.power(2, 8)
        self.assertEqual(p, 256)

    def testPowerInCorrect(self):
        p = test.power(2, 7)
        self.assertNotEqual(p, 256)


if __name__ == '__main__':
    unittest.main()
