def largest_of_three(list):
    return max(list)

numbers = [int(x) for x in input("Enter three numbers separated by space: ").split()]
result = largest_of_three(numbers)
print(f"The largest number among {numbers} is {result}.")