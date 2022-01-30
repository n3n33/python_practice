N, K = map(int, input().split())

list_a = list()

for i in range(1,N+1,1):
    if N % i == 0 :
        list_a.append(i)

if len(list_a) < K:
    print("0")
else:
    print(list_a[K-1])
