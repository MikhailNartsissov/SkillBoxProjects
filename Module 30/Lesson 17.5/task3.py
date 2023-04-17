from typing import List
from functools import reduce


def word_count(f_counter: int, f_string: str) -> int:
    if isinstance(f_counter, str):
        f_string += f_counter
        f_counter = 0
    for f_word in f_string.split():
        if f_word == 'was':
            f_counter += 1
    return f_counter


sentences: List[str] = ["Nory was a Catholic", "because her mother was a Catholic",
                        "and Nory’s mother was a Catholic",
                        "because her father was a Catholic",
                        "and her father was a Catholic",
                        "because his mother was a Catholic",
                        "or had been"
                        ]
print(reduce(word_count, sentences))
