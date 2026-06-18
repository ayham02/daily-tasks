def odd_or_even(num):
    if num & 1 == 0:
        return "Even"
    else:
        return "Odd"
    
input_num = int(input("Enter a number: "))
result = odd_or_even(input_num)
print(f"The number {input_num} is {result}.")
