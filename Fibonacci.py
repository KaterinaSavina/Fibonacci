def fib(n):
    if (n < 0):
        return("Index Error")
    else:
        index = 0
        fib = 0
        fib_new = 0
        middle = 1
        while index < n:
            fib_new = fib + middle
            fib = middle
            middle = fib_new
            index = index + 1
            print(fib)
        fib_new = str(fib)
        return(fib_new)
print(fib(8))
