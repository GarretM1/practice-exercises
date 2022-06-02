#!/usr/bin/python
import time
def fibi(n):

    a = 1
    b = 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for d in range(1, n):

            c = a + b
            a = b
            b = c

        return a


def fibr(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibi(n - 1) + fibr(n - 2)


n = int(input("Choose a value for n: "))
print(f"N chosen as {n}.")
t1 = time.perf_counter()
print(f"Iterative value at {n} is {fibi(n):e}")
t2 = time.perf_counter()
print(f"Iterative time {t2-t1:0.7f} seconds")
t3 = time.perf_counter()
print(f"Recursive value at {n} is {fibr(n):e}")
t4 = time.perf_counter()
print(f"Recursive time {t4-t3:0.7f} seconds")
