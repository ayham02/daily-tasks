def sort_by_age(dict_list):
    return sorted(dict_list, key=lambda x: x['age'])





people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

sorted_people = sort_by_age(people)
print(sorted_people)