import os


abs_path = os.path.abspath(os.path.join('..', '..', 'access', 'admin.bat'))
print('\nАбсолютный путь до файла: ', abs_path)
rel_path = os.path.join('Module 22', 'Lesson 9.1', 'access', 'admin.bat')
print('Относительный путь до файла: ', rel_path)
