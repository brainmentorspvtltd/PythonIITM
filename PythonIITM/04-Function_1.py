import time

def func_1():
    start = time.time()
    print("Hello")
    for i in range(100000):
        for j in range(10000):
            i + j
    end = time.time()
    print("Time taken",end-start)


func_1()
