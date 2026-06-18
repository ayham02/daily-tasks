def vowels(string):
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
result = vowels(input_string)
print(f"The number of vowels in the string '{input_string}' is {result}.")
