

def solution(n):
    fib1, fib2 = 0, 1
    
    for i in range(2, n+1):
        fib1, fib2 = fib2, fib1 + fib2
    
    return fib2 % 1234567