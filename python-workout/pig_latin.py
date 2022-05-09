def pig_latin():
    input_str = input('Enter the word : ')
    words = input_str.split()
    
    for words[0] in 'aeiou':
        input_str += 'way'
    print(input_str)