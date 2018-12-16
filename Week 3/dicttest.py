animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(len(animals.values()))
print(animals.keys())

values = animals.values()
sum = 0
for i in values:
    sum += len(i) 
print(sum)
