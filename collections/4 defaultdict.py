from collections import defaultdict

def default_dict(input_dict, x):
    result = defaultdict(list)
    for key, values in input_dict.items():
        filtered_values = [value for value in values if value > x]
        if filtered_values:
            result[key] = filtered_values
    return result


a = defaultdict(list, {'a': [1, 2, 3], 'b': [4, 1, 5], 'c': [0, 9]})
x_value = 2
print(default_dict(a, x_value))