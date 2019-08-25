import sys
from parser import checkArgs, checkGlobalSplit, parserLeft, parserRight
from reducer import reducerOne, reducerTwo, reducerThree
from solver import mainSolver

zeroDegreeR = []
firstDegreeR = []
secondDegreeR = []
zeroDegreeL = []
firstDegreeL = []
secondDegreeL = []

def assignTotalArray():
    ## zero degree left / right total
    totalArray = [0, 0, 0, 0, 0, 0]
    for index, obj in enumerate(zeroDegreeL):
        nbrZeroDegreeL= float((obj.content.split('*'))[0])
        totalArray[0] += (nbrZeroDegreeL * float(obj.sign))

    for index, obj in enumerate(zeroDegreeR):
        nbrZeroDegreeR = float((obj.content.split('*'))[0])
        totalArray[3] += (nbrZeroDegreeR * float(obj.sign))

    ## first degree left / right total
    for index, obj in enumerate(firstDegreeL):
        nbrFirstDegreeL= float((obj.content.split('*'))[0])
        totalArray[1] += (nbrFirstDegreeL * float(obj.sign))

    for index, obj in enumerate(firstDegreeR):
        nbrFirstDegreeR = float((obj.content.split('*'))[0])
        totalArray[4] += (nbrFirstDegreeR * float(obj.sign))

    ## second degree left / right total
    for index, obj in enumerate(secondDegreeL):
        nbrSecondDegreeL= float((obj.content.split('*'))[0])
        totalArray[2] += (nbrSecondDegreeL * float(obj.sign))

    for index, obj in enumerate(secondDegreeR):
        nbrSecondDegreeR = float((obj.content.split('*'))[0])
        totalArray[5] += (nbrSecondDegreeR * float(obj.sign))
    return totalArray


def main():
    if checkArgs(sys.argv) == True:
        mainArg = sys.argv[1]
    else:
        sys.exit()
    splitArg = mainArg.split()
    lenSplitArg = len(splitArg)
    equalPosition = checkGlobalSplit(splitArg, lenSplitArg)

    #Parser
    i = parserLeft(splitArg, equalPosition,zeroDegreeL, firstDegreeL, secondDegreeL)
    parserRight(splitArg, lenSplitArg, i, equalPosition, zeroDegreeR, firstDegreeR, secondDegreeR)

    if splitArg[i] == "=":
        sys.exit("Wrong Format, Can't solve")

    #Solver
    totalArray = assignTotalArray()
    reducerO = reducerOne(totalArray)
    reducerS = reducerTwo(totalArray, reducerO)
    totalFinalForm = []
    reducerT = reducerThree(totalArray, reducerS, totalFinalForm)

    print("a =", totalFinalForm[2])
    print("b =", totalFinalForm[1])
    print("c =", totalFinalForm[0])
 
    if reducerO == "0 = 0" or reducerS == "0 = 0" or reducerT == "0 = 0":
        print("All real R numbers are solutions")
        sys.exit()
    elif totalFinalForm[0] != 0 and totalFinalForm[1] == 0  and totalFinalForm[2] == 0:
        print("No solution")
        sys.exit()
    else:
        mainSolver(totalFinalForm)
   

if __name__== "__main__":
    main()
