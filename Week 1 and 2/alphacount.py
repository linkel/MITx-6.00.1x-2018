s = 'azcbobobegghakl'
longest = s[0]
longest2 = s[0]
for i in (range(1, len(s))):
    if s[i] >= longest[-1]:
        longest = longest + s[i]
    elif s[i] < longest[-1]:
        longest2 = s[i]
        for j in range(i+1,len(s)):
            if s[j] >= longest2[-1]:
                longest2 = longest2 + s[j]
            elif s[j] < longest2[-1]:
                break
    if (len(longest2) > len(longest)): #and (i > len(longest)):
        longest = longest2
        break

print("The longest alpha is: " + longest)