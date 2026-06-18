def second_largest(list):
    largest = 0
    second_largest = 0
    for i in list:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    return second_largest

input_list = [1, 2, 3, 4, 2, 5, 1]
print(second_largest(input_list))