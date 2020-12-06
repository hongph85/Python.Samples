def readint(prompt, min, max):
    while True:
        strVal = input(prompt)
        if strVal.isnumeric() == False:
            print("Wrong format. Input again.")
        else:
            return int(strVal)

def mySplit(str, spliter = " "):
    sPos = 0
    list = []
    while sPos < len(str) - 1 :
        ePos = str.find(spliter, sPos)
        if ePos == -1:
            return str

        if ePos == 0:
            return []

        word = str[sPos : ePos]
        list.append(word)
        sPos += len(word) + 1

    return list

def myPrint(arr):
    result = "["
    for item in arr:
        result += item + ", "

    return result[0:-1] + "]"
