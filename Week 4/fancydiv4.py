def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)

fancy_divide([0, 2, 4], 0)
#okay, so doing the 0 thing here just gives me the zero division error thing.
#if I do a 1 then I get a zero printed. Why? Raise Exception("0") just always executes if there isn't anything else wrong with the code?
#so it's only if I really do get a specific exception that I get the real exception printed. if the code is fine, it hits the raise exception always.
#if the code is not fine, then since it really hit a problem in the finally it gives the exception???? but doesn't it always go to the try? the except is higher in priority? 

#context is set to the last exception caught...maybe that has something to do with it. There seems to be IDE inconsistency too, to contend with. 