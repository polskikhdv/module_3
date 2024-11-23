data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def sum_data_structure(data):
    sum_ = 0
    for item in data:
        if isinstance(item, (int, float)):
            sum_ += item
        elif isinstance(item, str):
            sum_ += len(item)
        elif isinstance(item, (list, tuple, set)):
            sum_ += sum_data_structure(item)
        elif isinstance(item, dict):
            for key, value in item.items():
                sum_+= len(key)
                sum_ += value
    return sum_


print(sum_data_structure(data_structure))
