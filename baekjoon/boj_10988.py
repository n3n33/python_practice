#s = input()
strs = input()

# 소문자로 변환하여 저장
#for char in s:
    #if char.isalnum(): #영문자와 숫자 판별해 해당하는 문자만
#    strs.append(char.lower())
    
if strs == strs[::-1]:
    print("1")
else:
    print("0")
