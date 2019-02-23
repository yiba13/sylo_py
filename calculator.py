#!/usr/bin/env python3
import sys
#dict
#key 1-7 
#value is a list tax_ratio and sub
def calcule():
    try:
        salary = int(sys.argv[1])
    except:
        print("Parameter Error")
        return
    dictin = {1:[0.03,0],2:[0.1,105],3:[0.2,555],4:[0.25,1005],5:[0.3,2755],6:[0.35,5505],7:[0.45,13505]}
    s_sub = salary - 3500
    if s_sub <= 1500 :
        index = 1
    elif (s_sub>1500) and (s_sub <=4500) :
        index = 2
    elif 4500 <s_sub <=9000 :
        index = 3
    elif 9000 <s_sub <=35000 :
        index = 4
    elif 35000 <s_sub <=55000 :
        index = 5
    elif 55000 <s_sub <=80000 :
        index = 6
    else :
        index = 7
    tax = s_sub * dictin[index][0] - dictin[index][1]
    print(format(tax,".2f"))
    return 

if __name__ == "__main__":
    calcule()



