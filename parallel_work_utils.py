from multiprocessing import Pool, Process, Value
from ctypes import c_bool, c_long

from tqdm.auto import tqdm


class TqdmMultiprocessing:
    max_processes = 64

    def __init__(self, static_func, processes=64):
        self.counter = Value(c_long, lock=False)
        self.pool = Pool(
            processes=min(processes, self.max_processes),
            initializer=self.worker_init,
            initargs=(static_func, self.counter)
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pool.close()

    def tqdm(self, static_func, iterable, **kwargs):
        done_value = Value(c_bool)

        proc = Process(target=self.listener, args=(self.counter, done_value, kwargs,))
        proc.start()

        result = self.pool.map(static_func, iterable)

        done_value.value = True
        proc.join()
        self.counter.value = 0

        return result

    @staticmethod
    def listener(counter: Value, is_done: Value, kwargs):
        with tqdm(**kwargs) as tqdm_bar:
            old_counter = 0
            while not is_done.value:
                new_counter = counter.value
                tqdm_bar.update(new_counter - old_counter)
                old_counter = new_counter
            tqdm_bar.update(tqdm_bar.total - old_counter)

    @staticmethod
    def worker_init(static_func, counter: Value):
        static_func.counter = counter


def work(i):
    for _ in range(10**6):
        work.counter.value += 1
    return i


def main(n=1):
    with TqdmMultiprocessing(work, processes=3) as p:
        p.tqdm(work, range(n), total=n * 10 ** 6)
        p.tqdm(work, range(n), total=n * 10 ** 6)


if __name__ == "__main__":
    main(10)