import time

def fac(n):
    for i in range(2, n + 1): 
        print()
    # if n < 0:
    #     return None
    # if n < 1:
    #     return 1
    # return n * fac(n - 1)

x = time.perf_counter()
fac(5)
y = time.perf_counter()

print(y - x)