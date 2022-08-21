# Find the maximum of three numbers or more
def max_num(*args):
    return max(args)

# Multiply all the numbers in a list
def mult_list(numbers, product = 1):
    if not bool(len(numbers)):
        return 0
    
    for number in numbers:
        product *= number
    
    return product

# Reverse a string
def rev_string(string):
    return string[::-1]

# Check whether a number falls in a given range
def num_within(number, start, end):
    if number >= start and number <= end:
        return True
    
    return False

# Prints out the first n rows of Pascal's triangle
def pascal(n):
    if n >= 0 and n <= 5:
        for i in range(n):
            print(' '*(n - i), end='')

            number = str(11 ** i)
            number = list(number)
            
            print(' '.join(number))
    elif n > 5:
        for i in range(n):
            for j in range(n - i + 1):
                print(' ', end='')
            
            element = 1
            for j in range(1, i + 1):
                print(' ', element, sep='', end='')
                element = element * (i - j) // j
            print()
    else:
        print('Only numbers greater then 0.')


print(max_num(3, 5, 8))
print(mult_list([2, 5, 9]))
print(rev_string('continious'))
print(num_within(10, 2, 5))
pascal(6)