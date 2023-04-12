import os


dir_to_show = os.path.abspath(os.path.join('..', 'Lesson 9.1'))
print()

for i_elem in os.listdir(dir_to_show):
    path_to_file = os.path.abspath(os.path.join(i_elem))
    print('     ', path_to_file)
