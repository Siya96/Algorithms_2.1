import math
import random

class algo2Divide:
    def __init__(self):
        self.counter = 0

    def get3min(self, array):
        n = len(array)
        if n == 3:
            #self.counter += n * (int)(math.log2(n)) # T(n) for sorted() is O(nlogn)
            self.counter += n * (int)(math.log2(n))
            array = sorted(array)
            return array
        
        lefta = array[:n//2]
        righta = array[n//2:]
        left3min = self.get3min(lefta)
        right3min = self.get3min(righta)

        lst = left3min + right3min
        
        self.counter += len(lst) * (int)(math.log2(len(lst)))
        lst = sorted(lst)
        
        return lst[:3]

algo = algo2Divide()
a = []
k = 9
for i in range(1, 3*2**(k-1) + 1):
    a.append(i)
random.shuffle(a)
print(algo.get3min(a))
print(algo.counter)
