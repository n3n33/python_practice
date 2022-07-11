import sys

def topdown(lenth):
    num_list = []
    max_index = 0
    print("숫자 입력 하세요 : ")
    num_list = [sys.stdin.readline().strip() for _ in range(lenth)]

    for i in range(len(num_list)):
        max_index = i
        for j in range(i+1, len(num_list)):
            if num_list[max_index] < num_list[j]:
                max_index = j
        
        num_list[max_index], num_list[i] = num_list[i], num_list[max_index]
    
    for item in num_list:
        print(item)

topdown(3)