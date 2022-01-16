#!/usr/bin/env python

N = int(input())

array=[]

for i in range(N):
    array.append(input())

set_array=set(array)
array = list(set_array)	## 다시 list로 변환
array.sort()
array.sort(key = len)

for i in array:
    print(i)
