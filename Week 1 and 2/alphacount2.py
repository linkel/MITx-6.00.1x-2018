s = 'kpreasymrrs'
longest = s[0]
longestholder = s[0]
#go through the numbers of the range from the second letter to the end
for i in (range(1, len(s))):
    #if this letter is bigger or equal to the last letter in longest variable then add it on (meaning alphabetical order)
    if s[i] >= longest[-1]:
        longest = longest + s[i]
    #if this letter is smaller, meaning not in order, and so far longest is longer than my holder, then save longest into the holder and restart longest at my pointer
    elif s[i] < longest[-1] and (len(longestholder) < len(longest)):
        longestholder = longest
        longest = s[i]
    #if the letter is not in alpha order and longest ain't the longer one between it and holder then just start over
    elif s[i] < longest[-1]:
        longest = s[i]
#this last check is necessary for the case where we find the longest and it ends with the last letter, so it doesn't hit my elif check
if len(longestholder) < len(longest):
    longestholder = longest
print("Longest substring in alphabetical order is: " + longestholder)

#holy dingdongs man. Took me a full hour, and I had to look up that python can compare letters by their ascii value and get a bool. pretty convenient