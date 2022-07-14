import time


class Timer:
    _file = None

    @classmethod
    def set_file(cls, file_name):
        cls._file = file_name

    @staticmethod
    def get_time():
        return time.time(), time.process_time()


def log_time(function):
    def timed(*args, **kwargs):
        start_real, start_cpu = Timer.get_time()

        return_value = function(*args, **kwargs)

        end_real, end_cpu = Timer.get_time()

        cpu_time = end_cpu - start_cpu
        real_time = end_real - start_real

        if not Timer._file:
            print(
                f"[{function.__name__}] -> CPU time: {cpu_time:.4f} s, Real time: {real_time:.4f} s"
            )
        else:
            with open(f"./{Timer._file}", "at", encoding="utf-8") as _log:
                print(
                    f"[{function.__name__}] -> CPU time: {cpu_time:.6f} s, Real time: {real_time:.6f} s",
                    file=_log
                )

        return return_value
    return timed

