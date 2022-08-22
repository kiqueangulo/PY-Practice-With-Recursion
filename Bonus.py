def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        print(b, a % b)
        return greatest_common_divisor(b, a % b)

def arg_printer(a, b, bool = False, *args, **kwargs):
    print(a, b)
    print(bool)
    print(args)
    print(kwargs)


print(greatest_common_divisor(20, 23))
arg_printer(0, 1, 6, 5, 7, paramA = 20)