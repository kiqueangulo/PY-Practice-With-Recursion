# Write code for algorithm 5 below
def is_palindrome(string):
    return string == string[::-1]

def is_palindrome_iterable(string):
    backwards = list(string)
    backwards.reverse()

    for i in range(len(string)):
        if string[i] != backwards[i]:
            return False

    return True

def is_palindrome_recursive(string):
    if len(string) >= 2:
        if string[0] == string[-1]:
            return is_palindrome_recursive(string[1:-1])
        else:
            return False
    
    return True


print(is_palindrome('arepera'))
print(is_palindrome_iterable('perro'))
print(is_palindrome_recursive('radar'))
