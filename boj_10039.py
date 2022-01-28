num_sum = 0

for i in range(5):
    number = int(input())
    if number < 40:
        number = 40
        num_sum += number
    else:
        num_sum += number

print(num_sum//5)    
