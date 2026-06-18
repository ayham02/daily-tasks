def occurences(string):
    occurences = {}
    for char in string:
        if char in occurences:
            occurences[char] += 1
        else:
            occurences[char] = 1
    return occurences

input_string = input("Enter a string: ")
print(occurences(input_string))
