from random import randint


def change_dict(dct):
    num = randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            new_list = []
            new_list.extend(i_value)
            new_list.append(num)
            dct[i_key] = new_list
        if isinstance(i_value, dict):
            new_dict = dict()
            new_dict.update(i_value)
            new_dict[num] = i_key
            dct[i_key] = new_dict
        if isinstance(i_value, set):
            new_set = set()
            new_set.update(i_value)
            new_set.add(num)
            dct[i_key] = new_set


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}

print('--- Before function call ----')
print('nums_list =', nums_list)
print('some_dict =', some_dict)
print('uniq_nums =', uniq_nums)

print('\n--- Function call ----')
change_dict(common_dict)
print(common_dict)

print('\n--- After function call ----')
print('nums_list =', nums_list)
print('some_dict =', some_dict)
print('uniq_nums =', uniq_nums)
