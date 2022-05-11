import operator

PEOPLE = [{
    'first' : 'Reuven', 'last': 'Lerner',
    'email' : 'reuven@lerner.co.il'
    },{
    'first' : 'Donald', 'last': 'Trump',
    'email' : 'president@whitehoust.cgov'
    },{
    'first' : 'Vladimir', 'last': 'Putin',
    'email' : 'president@kremvax.ru'
    }
]

def alphabetize_names(dict_ex):
    return sorted(dict_ex, key=operator.itemgetter('last', 'first'))

print(alphabetize_names(PEOPLE))
