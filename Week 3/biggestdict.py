animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

#print(len(animals.values()))
#print(animals.keys())

values = animals.values()
keys = animals.keys()

starty = 0
for i in keys:
    bargle = len(animals[i])
    if bargle > starty:
        savest = i

print(savest)