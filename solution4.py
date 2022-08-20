# Write code for algorithm 4 below
def power(a, b):
    return a ** b

def recursive_power(a, b):
    if b == 0:
        return 1
    else:
        return a * recursive_power(a, b - 1)

print(power(2, 4))
print(recursive_power(2, 4))