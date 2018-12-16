def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    keys = aDict.keys()
    copykeys = list(aDict.keys())
    for item in keys:
        tempval = aDict[item]
        counter = 0
        for item2 in keys:
            firstitem = item2
            if aDict[item2] == tempval: 
                counter += 1
                if counter == 2:
                    if item2 in copykeys:
                        copykeys.remove(item2)
                    if item in copykeys:
                        copykeys.remove(item)
                
    return(copykeys)
            



dicky = {'vops':2, 'zips':1, 'bips':1, 'topple':5}
print(uniqueValues(dicky))
