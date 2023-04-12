matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for external_list_index in range(3):
    for internal_list_element in matrix[external_list_index]:
        print(internal_list_element, end=' ')
    print()
