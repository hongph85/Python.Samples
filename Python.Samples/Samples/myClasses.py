class Stack:
    """STack LIFO"""
    def __init__(self):
        self.__list = []
    def push(self, val):
        self.__list.append(val)
    def pop(self):
        return self.__list.pop(-1)

class SumOfStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        Stack.push(self, val)
        self.__sum += val

    def getSum(self):
        return self.__sum

class evenInterator():
    """description of class"""
    def __init__(self, list1):
        self.myList = list1
        self.myPos = 0
    def __iter__(self):
        return self

    def __next__(self):
        self.myPos+=1
        while self.myPos < len(self.myList):
            if self.myList[self.myPos-1]%2 == 0:
                return self.myList[self.myPos-1]
            else:
                self.myPos+=1
        else:
            raise StopIteration()