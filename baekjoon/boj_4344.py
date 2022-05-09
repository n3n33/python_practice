C = int(input())

for i in range(C):
    list_a = list(map(int, input().split()))
    avg = sum(list_a[1:])/list_a[0]    
    cnt  = 0
    
    for item in list_a[1:]:
        if item > avg:
            cnt += 1
            
    rate = (cnt/list_a[0]) * 100
    print('%.3f' %rate + '%')
