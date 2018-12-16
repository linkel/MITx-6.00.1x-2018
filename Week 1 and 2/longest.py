s = 'abcbcd'
store = s[0]
myStr = s[0]
for n in range(len(s)):
    if n != 0:
        if s[n] >= s[n-1]:
            myStr = myStr + s[n]
        if s[n] < s[n-1] and len(myStr) > len(store):
            store = myStr
            myStr = s[n]
    if n == 0:
        myStr = s[n]
if len(myStr) > len(store):
    store = myStr
print(store)