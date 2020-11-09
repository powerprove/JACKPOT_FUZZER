#!/usr/bin/env/python
# powerprove

def func():
    __import__('os')
    print dir()
    #print dir('os')

if __name__ == "__main__":
    func()
    print dir()
