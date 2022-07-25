import sys

n,m = map(int, sys.stdin.readline().split(' '))

used = [0 for _ in range(n+1)]
selected = [ 0 for _ in range(m+1)]

def rec_func(k):
    if k == m:
        for x in selected:
            sys.stdout.write(str(x)+ ' ')
        sys.stdout.write('\n')
    else:
        #####

        rec_func(k+1)

rec_func(0)