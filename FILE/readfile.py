#!/usr/bin/env python3

def readfile():
    filename=input("name:")
    file = open(filename)
    for x in file:
        print(x,end = '')
    file.close()

if __name__ == "__main__":
    readfile()
