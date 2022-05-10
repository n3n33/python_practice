def pig_latin(word):
    words = word.split()

    if words[0] in 'aeiou':
        return f'{word}way'
    else:
        return f'{words[1:]}{words[0]}ay'

print(pig_latin('test'))