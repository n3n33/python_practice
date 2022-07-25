#!/usr/bin/env python

def solution(arr):
    while True:
        # 저장
        arr = list(map(int, input().split()))
        # 전부 0이면 종료
        if arr[0] == arr[1] == arr[2] == 0 :
            break
        # 정렬
        tri = sorted(arr)
    
        if (tri[0]**2 + tri[1]**2) == tri[2]**2:
            print("right")
        else:
            print("wrong")
