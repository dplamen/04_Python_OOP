def cache(ref_func):
    log = {}

    def wrapper(n):
        if n in log:
            return log[n]
        else:
            log[n] = ref_func(n)
        return log[n]

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)
print(fibonacci.log)
