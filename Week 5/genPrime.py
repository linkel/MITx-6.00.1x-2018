def genPrimes():
    primeList = [2]
    checker = True
    n = 2
    yield n
    while True:
        n += 1
        checker = True
        for items in primeList:
            if (n % items) == 0:
                checker = False
        if checker == True:
            primeList.append(n)
            yield n

bicker = genPrimes()
print(bicker.__next__())
print(bicker.__next__())
print(bicker.__next__())
