from typing import List


class Person:
    """ Класс, экземпляры которого хранят информацию о человеке: его имя,
    возраст и остальные данные.
    """
    def __init__(self, c_name: str, c_age: int, c_is_black_mag: bool = False) -> None:
        self.__name = c_name
        self.__age = c_age
        self.__is_black_mag = c_is_black_mag

    def __str__(self):
        return '\nИмя: {name}\nВозраст: {age}\nЧёрный маг?: {is_mag}\n'.format(
            name=self.__name,
            age=self.__age,
            is_mag=self.__is_black_mag
        )

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, m_name: str) -> None:
        self.__name = m_name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, m_age: int) -> None:
        self.__age = m_age

    @property
    def is_black_mag(self) -> bool:
        return self.__is_black_mag

    @is_black_mag.setter
    def is_black_mag(self, m_is_black_mag: bool) -> None:
        self.__is_black_mag = m_is_black_mag


people: List[Person] = [Person('Вова', 55, True), Person('Петя', 25, True),
                        Person('Кузя', 34, True), Person('Ваня', 15, False)]
sorted_people = sorted(people, key=lambda element: element.age)
reverse_sorted_people = sorted(people, key=lambda element: element.age, reverse=True)

for person in sorted_people:
    print(person)

for person in reverse_sorted_people:
    print(person)
