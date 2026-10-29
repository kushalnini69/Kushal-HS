# Basic recursive factorial function with base case (n<=1) and recursive step
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

print(factorial(5))
print( factorial(0), factorial(1))
#------------------------------------------------
# Recursive factorial tracing call stack depth with space padding
def factorial(n, depth = 0):
    pad = " " * depth
    print(f"{pad} factorial {n} called")
    if n <= 1:
        print(f"{pad}-> base case returns 1")
        return 1
    result = n * factorial(n - 1, depth + 1)
    print(f"{pad} -> returns {result}")
    return result

factorial(4)
#-------------------------------------------------
# Infinite recursion bug demonstration (missing base case causing RecursionError)
def countdown(n):
    print(n)
    countdown(n - 1)

countdown(3)
#--------------------------------------
# Corrected recursive countdown with base case (n <= 0)
def countdown(n):
    if n <= 0:
        print("liftoff:")
        return
    print(n)
    countdown(n - 1)

countdown(3)
#-------------------------------------
# Recursive Fibonacci sequence generation
#FIBONACCI SERIES
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n-2)

for i in range(8):
    print(fib(i), end = " ")
#------------------------------------
# Compares iterative (loop-based) vs recursive factorial implementations
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

print(factorial_loop(5), factorial_rec(5))