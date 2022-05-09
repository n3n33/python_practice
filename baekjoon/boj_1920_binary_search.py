n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

for i in b:
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if mid < n and mid > -1:
            if a[mid] < i:
                low = mid + 1
            else:
                high = mid - 1
        else: break
    if mid < n and mid > -1:
        if i == a[high + 1]: 
            print(1)
        else: 
            print(0)
    else:
        print(0)
