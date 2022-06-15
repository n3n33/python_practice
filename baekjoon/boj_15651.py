import sys

#n, m = 4, 3
n,m = map(int, sys.stdin.readlines().split(' '))

selected = [ 0 for _ in range(m) ] # 0이 저장된 배열
used = [ 0 for _ in range(n+1) ] #0이 저장된 배열

def rec_func(k):
    if k == m:
        for  x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')

    else:
        for candidate in range(1,n+1):
            selected[k] = candidate
            rec_func(k+1)
            selected[k] = 0

rec_func(0)
