
def mysum(*numbers):
    tmp = 0
    for number in numbers:
        tmp += number
    print(tmp)


mysum(2,3,4)