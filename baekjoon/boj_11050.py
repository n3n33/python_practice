#!/usr/bin/env python

#import math 
import sys
n,k = map(int,sys.stdin.readline().split())

def fact(num):
     if num == 1: 
        return 1
     elif num == 0: 
        return 1
     else:
        return num * fact(num-1)
if k < 0:
    print("0")
elif k > n:
    print("0")
else:
    #result = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
    result = fact(n) // ( fact(k) * fact(n-k) )
    print(result)
