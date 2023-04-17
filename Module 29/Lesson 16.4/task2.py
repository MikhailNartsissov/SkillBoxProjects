from typing import Callable
from functools import wraps
from datetime import datetime
from time import sleep


def for_all_methods(decorator: Callable) -> Callable:
    @wraps(decorator)
    def decorate(cls):
        for f_method in dir(cls):
            if f_method.startswith('__') is False:
                f_method_name = getattr(cls, f_method)
                decorated_method = decorator(f_method_name)
                setattr(cls, f_method, decorated_method)
        return cls
    return decorate


def logging(f_function: Callable) -> Callable:
    @wraps(f_function)
    def wrapper(*args, **kwargs):
        print('Метод {name} вызван {time}'.format(name=f_function.__name__, time=datetime.now()))
        print('Аргументы метода:', args, kwargs)
        print('Документация метода:', f_function.__doc__)
        return f_function(*args, **kwargs)
    return wrapper


"""
Класс, описывающий стек.
Наследуется от списка.

Args:
    __object: передаётся элемент списка
"""


class Stack(list):
    def append(self, __object):
        super().insert(0, __object)

    def remove(self, __value=None):
        super().remove(self[0])


"""
Класс менеджера задач. 

Args:
    __stack: стек для хранения задач
"""


@for_all_methods(logging)
class TaskManager:
    def __init__(self):
        self.__stack = Stack()

    def new_task(self, m_task, m_priority):
        """
        Метод, добавляющий задачу в стек. Если задача с таким именем и приоритетом уже есть в стеке,
         не добавляется ничего.
        :param m_task: (str) имя задачи
        :param m_priority: (int) приоритет задачи
        :return:
        """
        if not (m_task, m_priority) in self.__stack:
            self.__stack.append((m_task, m_priority))

    def remove_task(self, m_task_name):
        """
        Метод, удаляющий задачу из стека. Используется вспомогательный стек
        для хранения задач, находящихся выше нужной.
        :param m_task_name: (str) имя задачи
        :return:
        """
        temp_list = Stack()
        while self.__stack[0][0] != m_task_name:
            temp_list.append(self.__stack[0])
            self.__stack.remove()
        if self.__stack[0][0] == m_task_name:
            self.__stack.remove()

        for task in temp_list:
            self.__stack.append(task)

    def __str__(self):
        """
        Метод для вывода на печать менеджера задач
        :return: (str) список задач в стеке, отсортированный и сгруппированный по приоритету
        """
        m_output_list = sorted(self.__stack, key=lambda item: item[1])
        m_current_index = None
        m_output_string = '\nРезультат:'
        for task in m_output_list:
            if str(task[1]) != m_current_index:
                m_current_index = str(task[1])
                m_output_string += '\n' + str(task[1]) + ' '
                m_output_string += task[0]
            else:
                m_output_string += '; ' + task[0]
        return m_output_string


task_manager = TaskManager()
task_manager.new_task('Поспать', 1)
sleep(2)
task_manager.new_task('Поесть', 2)
sleep(2)
task_manager.remove_task('Поесть')
sleep(2)
task_manager.remove_task('Поспать')
