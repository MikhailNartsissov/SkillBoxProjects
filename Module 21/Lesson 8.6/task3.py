def create_dict(f_data, template=None):
    if template is None:
        template = dict()
    if isinstance(f_data, dict):
        return f_data
    if isinstance(f_data, int) or isinstance(f_data, float) or isinstance(f_data, str):
        template[f_data] = f_data
        return template


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_dict = create_dict(i_element)
        if new_dict is not None:
            new_list.append(new_dict)
    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]

data = data_preparation(data)

print(data)
