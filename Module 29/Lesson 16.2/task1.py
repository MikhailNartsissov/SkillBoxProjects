from time import time
from contextlib import contextmanager
from _collections_abc import Iterator


@contextmanager
def timer() -> Iterator:
    start_time = time()
    try:
        yield
    except Exception as exc:
        print('Возникла ошибка', exc)
    finally:
        print('Время вычисления составило {duration} сек.'.format(
            duration=time()-start_time
        ))


with timer() as duration1:
    print('Первое выражение:')
    res1 = 888 * 88 ** 88888

with timer() as duration2:
    print('Второе выражение:')
    res2 = 999 * 99 ** 99999

with timer() as duration3:
    print('Третье выражение:')
    res3 = 1000 * 100 ** 100000
