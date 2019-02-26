#!/usr/bin/env python3


class Shiyanlou:
    __private_name = 'shiyanlou'
    def __get_private_name(self):
        return self.__private_name

if __name__ == "__main__":
    try:
        s = Shiyanlou()
        print("private")
    except:
        print("error")
    print(s._Shiyanlou__private_name)
