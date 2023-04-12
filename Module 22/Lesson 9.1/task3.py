import os

root_path = os.path.abspath('/')
print(root_path)

for list_element in os.listdir(root_path):
    print(list_element)
