A, B = map(int, input().split(' '))

revA = int(str(A)[::-1])
revB = int(str(B)[::-1])

C = revA+revB
revC = int(str(C)[::-1])
print(revC)
