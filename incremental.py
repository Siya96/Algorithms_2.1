import random

def OpCount():
    counter = 0
    a = []
    k = 5
    for i in range(1, 3*2**(k-1) + 1):
        a.append(i)
    random.shuffle(a)
    returns = find3Smallest(a, counter)
    print(returns[0], "took", returns[1], "operations!")
    

def find3Smallest(array, counter):
    if len(array) == 3:
        tupel = compare(array, counter)

        return (tupel[0], tupel[1])
    elm = array[0]
    returns = find3Smallest(array[1:], counter)
    triple = returns[0]
    counter = returns[1]
    triple.append(elm)
    i = 2
    while i >= 0:
        counter += 1
        if elm < triple[i]:
            triple[i+1] = triple[i]
            triple[i] = elm

        i -= 1
    return (triple[:-1], counter)


def compare(array, counter):
    counter += 1
    if array[1] < array[0]:
        temp = array[0]
        array[0] = array[1]
        array[1] = temp
    counter += 1
    if array [2] < array[1]:
        temp = array[1]
        array[1] = array[2]
        array[2] = temp
        counter += 1
        if array[1] < array[0]:
            temp = array[0]
            array[0] = array[1]
            array[1] = temp
    return (array, counter)
OpCount()