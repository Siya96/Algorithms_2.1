def maxkvot(array):
    n = len(array)
    
    if n == 2:
        return (array, array[1]/array[0])
    
    lefta = array[:n//2]
    righta = array[n//2:]
    leftkvot = maxkvot(lefta)
    rightkvot = maxkvot(righta)

    bestkvot = max(leftkvot[1], rightkvot[1])
    denominator = min(leftkvot[0])
    nominator = max(rightkvot[0])
    bestkvot = max(bestkvot, nominator/denominator)

    minmax = []
    lst = leftkvot[0] + rightkvot[0]
    lst = sorted(lst)
    minmax.append(lst[0])
    minmax.append(lst[3])

    return (minmax, bestkvot)

a = [80, 22, 20, 8, 40, 2, 10, 4]
print(maxkvot(a))
