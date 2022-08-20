# Write code for algorithm 2 belowdef count_to(number, start_number = 1):
def count_to(number, start_number = 1):
    if start_number <= number:
        print(start_number)
        count_to(number, start_number + 1)

count_to(5)