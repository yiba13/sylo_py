#!/usr/bin/env python3

class fib(n):
    current = 0
    a,b = 1,1
    while current < n:
        yield a
        a,b=b,a+b
        current+=1
if __name__ == '__main__':
    f5=fib(5)
    for x in f5:
        print(x)
