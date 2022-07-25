def pl_sentence(sentence):
    output = []
    for words in sentence.split():
        if words in 'aeiou':
            output.append(f'{words}way')
        else:
            output.append(f'{words[1:]}{words[0]}ay')
    return ' '.join(output)

print(pl_sentence('test test'))       
