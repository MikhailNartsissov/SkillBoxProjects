def sum_file_elements(f_filename):
    with open(f_filename, 'r', encoding='utf-8') as f_file:
        for f_line in f_file:
            f_nums = f_line.strip().split()
            for f_num in f_nums:
                yield int(f_num)


summ = 0
filename = 'numbers.txt'
str_to_write = '4 4 4\n5 5 5 5\n 6 6 6 6 6\n7 7 7 7'
with open(filename, 'w', encoding='utf-8') as num_file:
    num_file.write(str_to_write)
for element in sum_file_elements(filename):
    print(element)
    summ += element
    print(summ)
