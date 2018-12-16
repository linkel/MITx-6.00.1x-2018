def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    niceList = []
    for item in aDict.keys():
        checking = aDict[item]
        niceList.append(item)
        happened = 0
        for things in aDict.values():
            if checking == things:
                happened += 1
            if happened > 1:
                niceList.remove(item)
                break
    niceList.sort()
    return niceList
                

   

aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0, 2:44}

bDict = {1: 1, 2: 1, 3: 1}

print(uniqueValues(aDict))