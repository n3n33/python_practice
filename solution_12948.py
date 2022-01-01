#/usr/bin/env python
def solution(phone_number):
    answer = ''    
    for j in range(0,len(phone_number)-4):   
        answer+="*"      
    
    answer+=phone_number[len(phone_number)-4:len(phone_number)]
    return answer
