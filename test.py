#!/usr/bin/env python

def func(n):
    return n+1

def main():
    a = 3
    b = 5
    print("this: {0}".format(a+b))

    z = func(5)
    print(z)

if __name__ == "__main__":
    main()
