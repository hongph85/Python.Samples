import unittest
from sys import path
path.append("..\\Samples")
import Samples.myFunctions as my

class Test_MyFunctions(unittest.TestCase):
    def test_mySplit(self):
        print(my.myPrint(my.mySplit("To be or not to be, that is the question")))
        #self.assertEqual(print(list(my.mySplit("To be or not to be, that is the question"))),"['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']")
        #self.assertEqual(print(list(my.mySplit("To be or not to be,that is the question"))),"['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']")
        #self.assertEqual(print(list(my.mySplit("   "))),"[]")
        #self.assertEqual(print(list(my.mySplit(" abc "))),"['abc']")
        #self.assertEqual(print(list(my.mySplit(""))),"[]")

if __name__ == '__main__':
    unittest.main()
