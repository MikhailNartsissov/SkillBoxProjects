student_info = input('Введите в одну строку через пробел'
                     'фамилию, имя студента, город проживания, вуз, в котором он учится, '
                     'и все его оценки.\n\n'
                     )
student_data_list = student_info.split()
student_dict = dict()
student_dict['Фамилия'] = student_data_list[0]
student_dict['Имя'] = student_data_list[1]
student_dict['Город проживания'] = student_data_list[2]
student_dict['ВУЗ'] = student_data_list[3]
student_dict['Оценки'] = ' '.join(student_data_list[4:])
print('\nРезультат: ')
for student in student_dict:
    print(student, '-', student_dict[student])
