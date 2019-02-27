#!/usr/bin/env python3

class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __iter__(self):
        return self
    def __next__(self):
        self.a +=1
        if self.a > self.b:
            raise StopInteration()
        return self.a
if __name__ == '__main__':
    test = Test(0,5)
    print(next(test))
    print(next(test))
