import time


def get_time():
    return time.time(), time.process_time()


def log_time(function, _file=None):
    def timed(*args, **kwargs):
        start_real, start_cpu = get_time()

        return_value = function(*args, **kwargs)

        end_real, end_cpu = get_time()

        cpu_time = end_cpu - start_cpu
        real_time = end_real - start_real

        if not _file:
            print(
                f"[{function.__name__}] -> CPU time: {cpu_time:.4f} s, Real time: {real_time:.4f} s"
            )
        else:
            with open(f"./{_file}", "at", encoding="utf-8") as _log:
                print(
                    f"[{function.__name__}] -> CPU time: {cpu_time:.6f} s, Real time: {real_time:.6f} s",
                    file=_log
                )

        return return_value
    return timed

