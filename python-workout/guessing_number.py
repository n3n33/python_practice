import random 

def guessing_game():
    number = random.randint(0,101) # 0 ~ 100 
    input_number = int(input('Enter your number: '))
    if input_number < number:
        print('Too low')
    elif input_number > number:
        print('Too high')
    elif input_number == number:
        print('Just right')

guessing_game()
