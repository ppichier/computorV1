import re
import sys

class ClassDegree(object):
    def __init__(self, sign, content, degree):
        self.sign = sign
        self.content = content
        self.degree = degree

def checkArgs(args):
    argvLen = len(args)
    if argvLen == 2:
        return True
    elif argvLen > 2:
        print("Too much arguments")
        return False
    else:
        print("No argument provided")
        return False

def checkGlobalSplit(splitArg, lenSplitArg):
    if lenSplitArg < 3:
        print("Wrong format")
        sys.exit()
    try:
        equalPosition = splitArg.index('=')
    except ValueError:
        print("Wrong format")
        sys.exit()

    if equalPosition == lenSplitArg -1:
        print("Wrong format")
        sys.exit()
    
    return equalPosition

def parserLeft(splitArg, equalPosition, zeroDegreeL, firstDegreeL, secondDegreeL):
    endOfStr = 0
    i = 0
    if splitArg[0] == "0" and splitArg[1] == "=":
        endOfStr = 1
        i = 2
    elif re.search("^[-|+]?0+\.?0+$", splitArg[0]):
        endOfStr = 1
        i = 2
    if endOfStr == 0:
        i = 0
        while i < equalPosition:
            if (splitArg[i+2] == "X^0" or splitArg[i+2] == "x^0"):
                concatDegree = "0"
            elif (splitArg[i+2] == "X^1" or splitArg[i+2] == "x^1"):
                concatDegree = "1"
            elif (splitArg[i+2] == "X^2" or splitArg[i+2] == "x^2"):
                concatDegree = "2"
            else:
                sys.exit("Wrong Format, Can't solve")
            concatElement = "".join([splitArg[i] for i in range(i, i+3)])
            regexpSecondArg = re.search("^[-|+]?[0-9]+(\.[0-9]+)?\*([x|X]\^[0|1|2]){1}$", concatElement)
            if not regexpSecondArg or concatElement.count('*') != 1:
                sys.exit("Wrong Format, Can't solve")
            if i == 0:
                concatSign = "+1"
            else:
                precedentSign = splitArg[i -1] + "1"
                if precedentSign != '+1' and precedentSign != '-1':
                   sys.exit("Wrong Format, Can't solve")
                concatSign = precedentSign
            if concatDegree == "0":
                zeroDegreeL.append(ClassDegree(concatSign, concatElement, concatDegree))
            elif concatDegree == "1":
                firstDegreeL.append(ClassDegree(concatSign, concatElement, concatDegree))
            else:
                secondDegreeL.append(ClassDegree(concatSign, concatElement, concatDegree))
            i += 4
    return i

def parserRight(splitArg, lenSplitArg, i, equalPosition, zeroDegreeR, firstDegreeR, secondDegreeR):
    endOfStr = 0
    if splitArg[i] == "0" and i == lenSplitArg - 1:
        endOfStr = 1
    elif re.search("^[-|+]?0+\.?0+$", splitArg[i]):
        endOfStr = 1
    if endOfStr == 0:
        if lenSplitArg - i < 3 or lenSplitArg - i == 4 or ( (lenSplitArg - i - 3) % 4 != 0 and (lenSplitArg - i) != 3):
            sys.exit("Wrong Format, Can't solve")
        while i < lenSplitArg:
            if (splitArg[i+2] == "X^0" or splitArg[i+2] == "x^0"):
                concatDegree = "0"
            elif (splitArg[i+2] == "X^1" or splitArg[i+2] == "x^1"):
                concatDegree = "1"
            elif (splitArg[i+2] == "X^2" or splitArg[i+2] == "x^2"):
                concatDegree = "2"
            else:
                sys.exit("Wrong Format, Can't solve")

            concatElement = "".join([splitArg[i] for i in range(i, i+3)])
            regexpSecondArg = re.search("^[-|+]?[0-9]+(\.[0-9]+)?\*([x|X]\^[0|1|2]){1}$", concatElement)
            if not regexpSecondArg or concatElement.count('*') != 1:
                sys.exit("Wrong Format, Can't solve")
            if i == equalPosition + 1:
                concatSign = "+1"
            else:
                precedentSign = splitArg[i -1] + "1"
                if precedentSign != '+1' and precedentSign != '-1':
                    sys.exit("Wrong Format, Can't solve")
                concatSign = precedentSign
            if concatDegree == "0":
                zeroDegreeR.append(ClassDegree(concatSign, concatElement, concatDegree))
            elif concatDegree == "1":
                firstDegreeR.append(ClassDegree(concatSign, concatElement, concatDegree))
            else:
                secondDegreeR.append(ClassDegree(concatSign, concatElement, concatDegree))
            i += 4
            
