def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print(m)
    for i in range(n):
        g(n)

#what is the big O complexity?
#I answered n^2. I guess it's actually n.
# Is that because it is always just printing the same thing, so the only thing that affects the speed is the size of n, linearly? 

f(3)