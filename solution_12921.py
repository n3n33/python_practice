#!/usr/bin/env python

# 시간초과
# def solution(n):
#     answer = 0
#     for n in range(2, n+1):
#         for i in range(2, n):
#             if (n%i == 0):
#                 break
#         else:    
#             answer += 1
#     return answer

def solution(n):
    answer = set(range(2,n+1))
    
    for i in range(2,n+1):
        if i in answer:
            answer -= set(range(i*2,n+1,i))
    return len(answer)
