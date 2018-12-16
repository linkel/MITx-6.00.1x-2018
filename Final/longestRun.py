#Write a function called longestRun, which takes as a parameter a list of integers named L (assume L is not empty). 
#This function returns the length of the longest run of monotonically increasing numbers occurring in L. 
#A run of monotonically increasing numbers means that a number at position k+1 in the sequence is either greater than or equal to the number at position k in the sequence.

#For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should return the value 5 because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7].

def longestRun(L):
    saveList = []
    saveListTemp = []
    for n in range(len(L)):
        try:
            if L[n+1] >= L[n]:
                saveList.append(L[n])
            elif L[n+1] < L[n] and len(saveList) > len(saveListTemp):
                saveList.append(L[n])
                saveListTemp = saveList.copy()
                saveList = []
            elif L[n+1] < L[n] and len(saveList) <= len(saveListTemp):
                saveList = []
        except IndexError:
                saveList.append(L[n])
    if len(saveList) > len(saveListTemp):
        saveListTemp = saveList.copy()
    return len(saveListTemp)





Deff = [1, 1, 1, 6, 10]
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print(longestRun(Deff))