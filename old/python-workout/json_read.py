import json
import glob
import os

pwd = str(os.getcwd())
#print(f'{pwd}\9a.json')

#print(glob.glob(f'{pwd}\*.json'))

scores = []
names = os.path.basename(glob.glob(f'{pwd}\*.json'))
print(names)
scores[names] = {}
'''
for filename in os.path.basename(glob.glob(f'{pwd}\*.json')):
    scores[filename] = {}

    print(filename)
    with open(filename) as infile:
        for result in json.load(infile):
            for subject, score in result.items():
                scores[filename].setdefault(subject, [])
    #           scores[filename][subject].append(score)
'''
    
