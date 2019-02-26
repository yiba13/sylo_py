#!/usr/bin/env python3

class Animal:
    owner = 'jack'
    @property
    def age(self):
        return self.age
    @age.setter
    def age(self,value):
        if isinstance(value,int):
            self._age = value
        else:
            raise ValueError
    @staticmethod
    def order_animal_food():
        print("ording..")
        print("OK")

if __name__=="__main__":
    cat = Animal()
    try:
        cat.age = 'h'
    except:
        print("ValueError")
    cat.age=1
    print(cat._age) #Don`t suggest
    print(cat.owner)
    cat.order_animal_food()
