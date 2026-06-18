def duplicates(list):
    seen = set()
    result = []
    for i in list:
        if i in seen:
            result.append(i)
        else:
            seen.add(i)
    return result

input_list = [1, 2, 3, 4, 2, 5, 1]
print(duplicates(input_list))
