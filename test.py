#Question 1
import time

def func(a,b):
    time.sleep(5)
    return (a,b)
    
def timeit(myfunc,a,b):
    start = time.time()
    ans = myfunc(a,b)
    end = time.time()
    return (ans, end - start)
    
print(timeit(func, 1,2))
