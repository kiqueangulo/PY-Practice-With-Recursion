# Write code for algorithm 3 below
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def tribonacci(n):
    if n == 2:
        return 1
    elif n <= 1:
        return 0
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


print(fibonacci(6))
print(tribonacci(5))