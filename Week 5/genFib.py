def genFib():
    fib1 = 1
    fib2 = 0
    while True:
        next = fib1 + fib2
        yield next
        fib2 = fib1
        fib1 = next

fib = genFib()
print(fib.__next__())
print(fib.__next__())