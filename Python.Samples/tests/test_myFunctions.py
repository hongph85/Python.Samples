import unittest
from sys import path
path.append("..\\Samples")
import Samples.myFunctions as my

class Test_MyFunctions(unittest.TestCase):
    def test_mySplit(self):
        self.assertEqual(my.printStringArray(my.mySplit("To be or not to be, that is the question")),"['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']")
        self.assertEqual(my.printStringArray(my.mySplit("To be or not to be,that is the question")),"['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']")
        self.assertEqual(my.printStringArray(my.mySplit("   ")),"[]")
        self.assertEqual(my.printStringArray(my.mySplit(" abc ")),"['abc']")
        self.assertEqual(my.printStringArray(my.mySplit("")),"[]")

if __name__ == '__main__':
    unittest.main()
