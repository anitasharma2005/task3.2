def print_positive_numbers(input_list):
positive_numbers = [num for num in input_list if num > 0]
print("Input:", input_list)
print("Output:", positive_numbers)
list1 = [12, -7, 5, 64, -14]
print_positive_numbers(list1)
list2 = [12, 14, -95, 3]
print_positive_numbers(list2)