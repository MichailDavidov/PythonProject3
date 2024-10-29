def calculate_structure_sum(data_structure):
    list_ = []
    if not any(isinstance(elem, (set, tuple, list, dict)) for elem in data_structure):
        return sum([int(i) if isinstance(i, int)
                    else len(i) if isinstance(i, str)
                    else calculate_structure_sum([i]) for i in data_structure])
    for elem in data_structure:
        if isinstance(elem, (list, tuple, set)):
            list_.extend(elem)
        elif isinstance(elem, dict):
            list_.extend(elem.values())
            list_.extend(elem.keys())
        elif isinstance(elem, int) or isinstance(elem, str):
            list_.append(elem)

    return sum([int(i) if isinstance(i, int)
                else len(i) if isinstance(i, str)
                else calculate_structure_sum([i]) for i in list_])


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)







