#!/usr/bin/env python
while True:
    num = input()
    #num_list = list(map(int, str(num)))
    
    if num == '0' :
        break
    if num == num[::-1]:
        print('yes')
    else:
        print('no')

