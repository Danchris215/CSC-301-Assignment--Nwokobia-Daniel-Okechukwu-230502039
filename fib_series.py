def fib_series(n):
    if n <= 1:
        return n
    
    return fib_series(n-1) + fib_series(n-2)


print(fib_series(8))