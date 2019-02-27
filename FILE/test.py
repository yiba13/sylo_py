#!/usr/bin/env python3

def readflines():
    filename=input("name:")
    with open(filename) as file:
        count=0
        for line in file:
            count +=1
            print(line)
    print("lines",count)

if __name__ == "__main__":
    readflines()
