from contextlib import contextmanager
from _collections_abc import Iterator
from os import getcwd, chdir, listdir


@contextmanager
def in_dir(f_path: str) -> Iterator:
    f_current_dir = getcwd()
    try:
        chdir(f_path)
        yield
    except Exception as exc:
        print('Возникла ошибка', exc)
    finally:
        chdir(f_current_dir)


print(getcwd())
with in_dir('/usr') as new_dir:
    print(getcwd())
    print(listdir())
print(getcwd())
