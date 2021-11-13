import time


def exec_time(ref_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ref_func(*args, **kwargs)
        end_time = time.time()
        return end_time - start_time
    return wrapper


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
