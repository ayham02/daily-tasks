def reverse(string):
    if (len(string) <=1 ):
        return string
    
    return  reverse(string[1:]) + string[0]

input_string = input("Enter a string: ")
result = reverse(input_string)
print(f"The reverse of the string '{input_string}' is '{result}'.")
