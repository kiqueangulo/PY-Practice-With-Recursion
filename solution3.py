# Write code for algorithm 3 below
def fibonacci_element(n):
    if n <= 1:
        return n
    else:
        return fibonacci_element(n - 1) + fibonacci_element(n - 2)
        
print(fibonacci_element(6))