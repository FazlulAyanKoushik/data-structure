from functools import reduce

numbers = [1, 2, 3, 4, 5]


# Using reduce() to compute sum of list
def my_sum(x, y):
    return x + y


sum_of_numbers = reduce(my_sum, numbers)

# Using lambda function

sum_of_numbers_by_lamda = reduce(lambda x, y: x + y, numbers)

print("numbers: ", numbers)
print("sum_of_numbers: ", sum_of_numbers)
print("sum_of_numbers_by_lamda: ", sum_of_numbers_by_lamda)
