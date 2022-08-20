# Accepts any number of named arguments and prints them in the pattern key : value one at a time
def name_args(**kwargs):
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

# Returns True if all the elements in an iterable are true
def all_true(elements):
    return all(elements)

# Returns True if one of the elements in an iterable is true
def one_true(elements):
    return any(elements)

# Uses recursion to find the factorial of an integer
def recursive_factorial(number):
    if number > 1:
        return number * recursive_factorial(number - 1)
    
    return 1

# Recursively removes all adjacent duplicate letters from a string
def recursive_duplicate(string, i = 0):
    if len(string) <= 1 or i == len(string) - 1:
        return string
    else:
        if string[i] != string[i + 1]:
            return recursive_duplicate(string, i + 1)
        
        return recursive_duplicate(string[0:i] + string[i + 1:], i)

# Uses recursion to reverse a string
def recursive_reverse(string, i = 0):
    if len(string) != 0:
        if i == len(string) - 1:
            return string[0]
        
        return string[-1 - i] + recursive_reverse(string, i + 1)
    
    return ""

name_args(name = 'Pablo', age = 22, title = 'Software Dev')
print(all_true(["a", 1, True]))
print(one_true(["", 1, False]))
print(recursive_factorial(4))
print(recursive_duplicate("aabbccddAABBB"))
print(recursive_reverse('apple'))