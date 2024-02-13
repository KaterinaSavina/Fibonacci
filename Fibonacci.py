def fib(n):
    n = int(n)
    if (n < 0):
        return("Порядковый номер - это положительное число")
    else:
        index = 0
        fib = 0
        middle = 1
        while index < n:
            fib_new = fib + middle
            fib = middle
            middle = fib_new
            index = index + 1
        return(fib)

index = input("Введите № числа Фибоначчи ")
print(fib(index))
