def ft_sqrt(nb):
    i = 0
    precision = 4
    while i * i < nb:
    	i += 1
    	if i * i >= nb:
    	    break
    if  i == 0 or i * i == nb:
        return i
    else:
        i -= 1
    increment = 0.1
    for x in range(0, precision):  
        while (i * i <= nb): 
            i += increment 
        i -= increment 
        increment /= 10
    return i


def solverFirstDegree(totalFinalForm):
    print("Polynomial degree: 1")
    if totalFinalForm[0] == 0:
        print("The solution is:\n0")
    else:
        solutionPolynome = -totalFinalForm[0] / totalFinalForm[1]
        print("The solution is:\n", solutionPolynome)

def solverSecondDegree(totalFinalForm):
    print("Polynomial degree: 2")
    discriminant = totalFinalForm[1] * totalFinalForm[1] - 4 * totalFinalForm[2] * totalFinalForm[0]
    print("The discriminant is :", discriminant)
    if discriminant == 0:
        solutionPolynome = -totalFinalForm[1] / (2 * totalFinalForm[2])
        if isinstance(solutionPolynome, float) and (solutionPolynome).is_integer():
            solutionPolynome = int(solutionPolynome)
        print("One unique solution x0:")
        print(solutionPolynome)
    elif discriminant > 0:
        print("Two solutions:")
        solutionPolynome = [0, 0]
        sqrtDicriminant = ft_sqrt(discriminant)
        solutionPolynome[0] = (-totalFinalForm[1] - sqrtDicriminant) / (2 * totalFinalForm[2])
        solutionPolynome[1] = (-totalFinalForm[1] + sqrtDicriminant) / (2 * totalFinalForm[2])
        if isinstance(solutionPolynome[0], float) and (solutionPolynome)[0].is_integer():
            solutionPolynome[0] = int(solutionPolynome[0])
        if isinstance(solutionPolynome[1], float) and (solutionPolynome)[1].is_integer():
            solutionPolynome[1] = int(solutionPolynome[1])
        print("x1: %.2f" %(solutionPolynome[0]))
        print("x2: %.2f" %(solutionPolynome[1]))
    else:
        print("Two solutions complexes:")
        sqrtDicriminant = ft_sqrt(-discriminant)
        if isinstance(totalFinalForm[1], float) and (totalFinalForm[1]).is_integer():
            totalFinalForm[1] = int(totalFinalForm[1])
        if isinstance(totalFinalForm[2], float) and (totalFinalForm[2]).is_integer():
            totalFinalForm[2] = int(totalFinalForm[2])
        print("x1:", -totalFinalForm[1], "/", 2 * totalFinalForm[2], "- i", "%.2f" %(sqrtDicriminant), "/", 2 * totalFinalForm[2] )
        print("x2:", -totalFinalForm[1], "/", 2 * totalFinalForm[2], "+ i", "%.2f" %(sqrtDicriminant),"/", 2 * totalFinalForm[2] )

def mainSolver(totalFinalForm):
    if totalFinalForm[2] == 0:
        solverFirstDegree(totalFinalForm)
    else:
        solverSecondDegree(totalFinalForm)