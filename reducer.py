def only_element(index, totalArray):
    if index == 0 or index == 3:
        return True
    cpt = 0
    i = index - 1
    limit = 0 if index < 3 else 3
    target = index - limit
    while i >= limit:
        cpt += 1 if totalArray[i] == 0 else 0
        i -= 1
    if cpt == target:
        return True
    return False

def reducerOne(totalArray):
    reduceFormOne = ""
    for index,x in enumerate(totalArray):
        reduceFormOneOperator = " + "
        if index == 0 or index == 3:
            reduceFormOneDegree = "X^0"
        elif index == 1 or index == 4:
            reduceFormOneDegree = "X^1"
        elif index == 2 or index == 5:
            reduceFormOneDegree = "X^2"
        if isinstance(x, float) and (x).is_integer():
            x = int(x)
        if only_element(index, totalArray) or x == 0:
            reduceFormOneOperator = ""
        if (index != 0 and index != 3) and x < 0:
            x = -x
            if only_element(index, totalArray):
                reduceFormOneOperator = "-"
            else:
                reduceFormOneOperator = " - "      
        if (x != 0):
            reduceFormOne += reduceFormOneOperator + str(x) + " * " + reduceFormOneDegree 
        if index == 2:
            if len(reduceFormOne) == 0:
                reduceFormOne += "0"
            reduceFormOne += " = "
        if index == 5 and reduceFormOne[len(reduceFormOne) - 2] == "=":
            reduceFormOne += "0"

    print("Reduced form 1 :", reduceFormOne)
    return reduceFormOne

def reducerTwo(totalArray, reducerOne):
    reduceFormTwo = ""
    totalArray[3] = -totalArray[3]
    totalArray[4] = -totalArray[4]
    totalArray[5] = -totalArray[5]
    totalArray[1], totalArray[3] = totalArray[3], totalArray[1] 
    totalArray[2], totalArray[4] = totalArray[4], totalArray[2]
    totalArray[2], totalArray[3] = totalArray[3], totalArray[2]
    for index,x in enumerate(totalArray):
        reduceFormTwoOperator = " + "
        if index == 0 or index == 1:
            reduceFormTwoDegree = "X^0"
        elif index == 2 or index == 3:
            reduceFormTwoDegree = "X^1"
        elif index == 4 or index == 5:
            reduceFormTwoDegree = "X^2"
        if isinstance(x, float) and (x).is_integer():
            x = int(x)
        if x == 0 or index == 0 or len(reduceFormTwo) == 0:
            reduceFormTwoOperator = ""
        elif index != 0 and x < 0:
            x = -x
            reduceFormTwoOperator = " - "
        if (x != 0):
            reduceFormTwo+= reduceFormTwoOperator + str(x) + " * " + reduceFormTwoDegree
        if index == len(totalArray) - 1:
            if len(reduceFormTwo) == 0:
                reduceFormTwo += "0"
            reduceFormTwo += " = 0"

    if reduceFormTwo != reducerOne:
        print("Reduced form 2 :", reduceFormTwo)
    return reduceFormTwo

def reducerThree(totalArray, reducerThree, totalFinalForm):
    reduceFormThree = ""
    i = 0
    while i < len(totalArray):
        reduceFormThreeOperator = " + "
        if i == 0:
            reduceFormThreeDegree = "X^0"
        elif i == 2:
            reduceFormThreeDegree = "X^1"
        elif i == 4:
            reduceFormThreeDegree = "X^2"
        totalThreeForm = totalArray[i] + totalArray[i + 1]
        totalFinalForm.append(totalThreeForm)
        if isinstance(totalThreeForm, float) and (totalThreeForm).is_integer():
            totalThreeForm = int(totalThreeForm)
        if totalThreeForm == 0 or i == 0 or len(reduceFormThree) == 0:
            reduceFormThreeOperator = ""
        elif i != 0 and totalThreeForm < 0:
            totalThreeForm = -totalThreeForm
            reduceFormThreeOperator = " - "
        if totalThreeForm != 0:
            reduceFormThree+= reduceFormThreeOperator + str(totalThreeForm) + " * " + reduceFormThreeDegree
        if i == len(totalArray) - 2:
            if len(reduceFormThree) == 0:
                reduceFormThree += "0"
            reduceFormThree += " = 0"
        i += 2
    if reduceFormThree != reducerThree:
        print("Reduced form 3 :", reduceFormThree)
    return reduceFormThree