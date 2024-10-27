from collections import OrderedDict

def ordered_dict(x):
    ord_dict = OrderedDict()
    index = 0
    for value in x:
        ord_dict[value] = index
        index += 1
    return ord_dict


a = ['red', 'green', 'pink', 'black']
print(ordered_dict(a))
