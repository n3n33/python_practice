#!/usr/bin/env python
def solution(numbers):
    answer = -1
    
    num = 45
    tmp = 0     
    for item in range(len(numbers)):
        tmp += numbers[item]
    
    answer = num - tmp
    return answer
