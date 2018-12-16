s = 'bobthebob'
searchfor = 'bob'
bobcount = 0
slength = len(searchfor)
for n in range(len(s)):
    if s[n:n+slength] == searchfor:
        bobcount += 1

print('Bobcount is ' + str(bobcount))