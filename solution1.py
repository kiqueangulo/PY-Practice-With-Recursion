# Write code for algorithm 1 below
def print_to_zero(number):
    if number == 0:
        print(0)
    elif number < 0:
        print(number)
        print_to_zero(number + 1)
    else:
        print(number)
        print_to_zero(number - 1)

print_to_zero(5)