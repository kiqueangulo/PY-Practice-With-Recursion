def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        print(b, a % b)
        return greatest_common_divisor(b, a % b)

print(greatest_common_divisor(20, 23))