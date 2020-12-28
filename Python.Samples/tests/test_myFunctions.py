import unittest
from sys import path
path.append("..\\Samples")
import Samples.myFunctions as my
from Samples.myClasses import Stack, SumOfStack, evenInterator
from Samples.classInheritance import Sub
from random import randint, randrange
import os
import types
import time

class Test_MyFunctions(unittest.TestCase):
    def test_mySplit(self):
        self.assertEqual(my.printStringArray(my.mySplit("To be or not to be, that is the question")),"['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']")
        self.assertEqual(my.printStringArray(my.mySplit("To be or not to be,that is the question")),"['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']")
        self.assertEqual(my.printStringArray(my.mySplit("   ")),"[]")
        self.assertEqual(my.printStringArray(my.mySplit(" abc ")),"['abc']")
        self.assertEqual(my.printStringArray(my.mySplit("")),"[]")

    def test_readFile(self):
        text = my.openAndReadFile('hongph.txt')
        self.assertEqual(text, 'Hello HongPH!')
        text1 = my.openAndReadFile('hongph.txt', 5)
        self.assertEqual(text1, 'Hello')

    def test_writeFile(self):
        text = 'hello1234'
        path = 'hong33.txt'
        my.createFile(path, text)
        self.assertTrue(os.path.exists(path))
        self.assertEqual(text, open(path, 'r').read())

    def test_SpliceString(self):
        # Slices
        alpha = "abdefg"
        self.assertEqual(alpha[1:3], 'bd')
        self.assertEqual(alpha[3:], 'efg')
        self.assertEqual(alpha[:3], 'abd') # abd
        self.assertEqual(alpha[3:-2], 'e') #e
        self.assertEqual(alpha[-3:4], 'e') #e
        self.assertEqual(alpha[::2], 'adf') # adf
        self.assertEqual(alpha[1::2], 'beg') #beg
        self.assertEqual(alpha[-1:0:-1], 'gfedb') #gfedb
        self.assertEqual(alpha[-2: 0], '') #empty

        # Demonstrating the split() method:
        print("phi       chi\npsi")
        print("phi       chi\npsi".split())

    def test_CompareString(self):
         self.assertTrue("10" > "010")
         self.assertTrue("10" < "8")
         self.assertTrue("20" < "8")
         self.assertTrue("20" < "80")
         self.assertRaises(TypeError, lambda: "10" > 10)

         self.assertTrue('smith' > 'Smith')
         self.assertFalse('Smiths' < 'Smith')
         self.assertTrue('Smith' > '1000')
         self.assertTrue('11' < '8')

    def test_Stack(self):
         stack = Stack()
         stack.push(1)
         stack.push(2)

         self.assertTrue(2 == stack.pop())
         self.assertTrue(1 == stack.pop())

    def test_NewStack(self):
         stack1 = SumOfStack()
         stack1.push(1)
         stack1.push(2)

         self.assertTrue(3 == stack1.getSum())
    
    def test_Random(self):
        for i in range(0,100):
            self.assertTrue(randrange(0, 1, 1) == 0) # random in range 0, 1 but not include 1
            self.assertIn(str(randint(0,1)), "01") # random in range 0, 1 include 1
    
    def test_Inheritance(self):
        sub = Sub()
        self.assertTrue(sub.fun_a()==11)
        self.assertTrue(sub.fun_b() == 22)
        self.assertTrue(sub.fun() == "fun of SuperA")

    def test_listComprehensive(self):
        list1 = []
        for x in range(6):
            list1.append(10**x)

        list2 = [10**x for x in range(6)]
        self.assertEquals(list1,list2)

    def test_listComprehensive1(self):
        list1 = [1 if x%2 == 0 else 0 for x in range(10)]
        list2 = {1 if x%2 == 0 else 0 for x in range(10)}
        list3 = (1 if x%2 == 0 else 0 for x in range(10))

        print(list1)
        self.assertTrue(type(list1) is list)
        self.assertTrue(type(list2) is set)
        self.assertTrue(isinstance(list3, types.GeneratorType))

    def test_closure(self):
        a = my.makeClosure(1)
        b = my.makeClosure(2)
        
        self.assertTrue(a(2)==1)
        self.assertTrue(b(2)==4)
        for i in range(3):
            print(a(i), b(i), end=" ")
            print()

    def test_lambda(self):
        a = [x for x in range(10)]
        even = my.getEvenList(a)
        b = my.getPow2OfList(a)

        self.assertEquals(even, [0,2,4,6,8])
        self.assertEquals(b, [0,1,4,9,16,25,36,49,64, 81])

    def test_getEvenGenerator(self):
        a = [x for x in range(10)]
        even = evenInterator(a)
        for x in even:
            print(x, end=" ")

    def test_manipulateString(self):
        self.assertTrue(str(1-1)=="0")
        self.assertTrue('0123456789'[:2]=="01")
        self.assertFalse(str(1-1) not in '012345₤789'[:2])
        self.assertTrue('abcd'[::-1]=="dcba")
        self.assertTrue('!'+'2'*2=="!22")
        self.assertFalse('1'+'1'+'1'<'1'*3)
        self.assertTrue('012'[-1:0]=="")
        self.assertTrue('012'[0:-1]=="01")
        self.assertTrue('012'[-1:-2]=="")
        self.assertTrue('012'[-1:2]=="")

    def test_datetime(self):
        timestamp1 = 1572879180
        timeStruct = time.gmtime(timestamp1)
        self.assertEqual(time.asctime(timeStruct), "Mon Nov  4 14:53:00 2019")

        timestamp2 = time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0))
        self.assertEqual(time.ctime(timestamp2), "Mon Nov  4 14:53:00 2019")

    def test_mkdir(self):
        self.assertRaises(FileExistsError, lambda: os.mkdir("a/b/c/d"))
        

if __name__ == '__main__':
    unittest.main()
