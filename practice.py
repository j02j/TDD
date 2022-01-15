import unittest

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def division(a, b):
    return a / b

def multiply(a, b):
    return a * b

class TddTest(unittest.TestCase):
    
    aa = 0
    bb = 0
    result = 0

    def setUp(self):
        self.aa = 10
        self.bb = 20

    def testAdd(self):
        self.result = add(self.aa, self.bb)

        self.assertEqual(self.result, 31)

    def testSubstract(self):
        self.result = substract(self.aa, self.bb)

        if self.result > 10:
            boolval = True
        else:
            boolval = False

        self.assertTrue(boolval)

    def testDivision(self):
        self.assertRaises(ZeroDivisionError, division, 4, 1)

    def testMultiply(self):
        nonechk = True

        self.result = multiply(10, 9)

        if self.result > 100:
            nonechk = None

        self.assertIsNone(nonechk)

    def tearDown(self):
        print(' 결과 값 : ' + str(self.result))

if __name__ == '__main__':
    unittest.main()
