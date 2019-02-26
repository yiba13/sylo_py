#!/usr/bin/env python3

class Animal:
    @property
    def age(self):
        return self.age
    @age.setter
    def age(self,value):
        if isinstance(value,int):
            self._age = value
        else:
            raise ValueError

if __name__=="__main__":
    cat = Animal()
    try:
        cat.age = 'h'
    except:
        print("ValueError")
    cat.age=1
    print(cat._age) #Don`t suggest
