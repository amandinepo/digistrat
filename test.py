#Question 1
import time
from itertools import combinations

def func(a,b):
    time.sleep(5)
    return (a,b)
    
def timeit(myfunc,a,b):
    start = time.time()
    ans = myfunc(a,b)
    end = time.time()
    return (ans, end - start)
    
print(timeit(func, 1,2))

#Question 2
def subarray(tab: list, k: int):
    comb = list(combinations(tab, k))
    count = 1
    # on élimine 
    for i in range(1,len(tab)):
        count = count + 1 if (tab[i] != tab[i-1]) else count
    return 

l = [2,2,1,1,3]
print(subarray(l, 3))
