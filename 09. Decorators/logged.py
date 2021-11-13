def logged(ref_func):
    def wrapper(*args):
        result = f'you called {ref_func.__name__}{args}\n'
        result += f'it returned {ref_func(*args)}'
        return result
    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
