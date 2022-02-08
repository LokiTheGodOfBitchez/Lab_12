#!/usr/bin/env python3
# -*- coding: utf-8 -*-


x = float(input("Write x: "))
n = int(input("Write n: "))


def rec(x, n):
    if n == 0:
        print(1)
        return
    elif n < 0:
        x = 1/x**(abs(n))
        print(x)
        return
    elif n > 0:
        x = x * (x**(n-1))
        print(x)
        return


if __name__ == '__main__':
    rec(x, n)
