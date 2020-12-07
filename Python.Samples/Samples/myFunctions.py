def readint(prompt, min, max):
    while True:
        strVal = input(prompt)
        if strVal.isnumeric() == False:
            print("Wrong format. Input again.")
        else:
            return int(strVal)

def mySplit(str):
    # return empty if only spaces
    if str.isspace() or len(str)==0:
        return []

    str = str.lstrip().rstrip()
    spliter = " "
    sPos = 0
    list = []


    ePos = str.find(spliter, sPos)
    # if does not find any space return the list with on an item
    if ePos == -1:
        list.append(str)
        return list

    while True:
        # if start with space
        ePos = str.find(spliter, sPos)
        # if the next word end with "\r\n"
        
        if ePos == -1:
            epos = str.find("\r\n", sPos)
            word = str[sPos:]
        else:
            word = str[sPos : ePos]
        if word != "":
            list.append(word)
        sPos += len(word) + 1
        if sPos > len(str):
            break

    return list

def printStringArray(arr):
    if len(arr) == 0:
        return "[]"
    result = "["
    for item in arr:
        result += "'" + item + "', "

    return result[0:-2] + "]"
