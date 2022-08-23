def sum_possible(target, numbers):
    if target > 0 and len(numbers) > 0:        
        for i in range(len(numbers) - 1):
            for j in range(1, len(numbers)):
                if any([
                    target % numbers[i] == 0 or target % numbers[j] == 0,
                    target - numbers[i] >= numbers[j] and (target - numbers[i]) % numbers[j] == 0,
                    target - numbers[j] >= numbers[i] and (target - numbers[j]) % numbers[i] == 0
                ]):
                    return True
    
    if len(numbers) == 1 and target % numbers[0] == 0:
        return True
    
    return False

def recursive_sum_possible(target, numbers, start = 1):
    if target == 0 or len(numbers) == 0:
        return "Nothing to sum"

    if len(numbers) != 1 and start < len(numbers):
        if any([
            target % numbers[0] == 0 or target % numbers[start] == 0,
            target - numbers[0] >= numbers[start] and (target - numbers[0]) % numbers[start] == 0,
            target - numbers[start] >= numbers[0] and (target - numbers[start]) % numbers[0] == 0
        ]):
            return True
        
        recursive_sum_possible(target, numbers, start + 1)
    
    if len(numbers) != 1:
        recursive_sum_possible(target, numbers[1:])
    
    return False
            

print(sum_possible(8, [5, 12, 4]))         # True -> 2(4) = 8
print(sum_possible(15, [6, 2, 10, 19]))    # False
print(sum_possible(271, [10, 8, 265, 24])) # False
print(sum_possible(13, [3, 5]))            # True -> 3 + 2(5) = 0
print(sum_possible(43, [7, 11, 3, 9, 36])) # True -> 7 + 4(9) = 43
print(sum_possible(58, [7, 26, 3]))        # True -> 7(7) + 3(3) = 58
print(sum_possible(24, []))              # False
print(sum_possible(12, [12]))              # True

# print(recursive_sum_possible(8, [5, 12, 4]))
# print(recursive_sum_possible(15, [6, 2, 10, 19]))
# print(recursive_sum_possible(271, [10, 8, 265, 24]))
# print(recursive_sum_possible(13, [3, 5]))
# print(recursive_sum_possible(43, [7, 11, 3, 9, 36]))
# print(recursive_sum_possible(58, [7, 26, 3]))