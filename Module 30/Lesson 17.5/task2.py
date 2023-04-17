from typing import List


result_list: List[str] = list(filter(lambda symbol: not symbol.isdigit() and not symbol.isupper(),
                                     list(input('Введите строку:').strip())))
