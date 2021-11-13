def make_bold(ref_func):
    def wrapper(*args, **kwargs):
        return '<b>' + ref_func(*args, **kwargs) + '</b>'
    return wrapper


def make_italic(ref_func):
    def wrapper(*args, **kwargs):
        return '<i>' + ref_func(*args, **kwargs) + '</i>'
    return wrapper


def make_underline(ref_func):
    def wrapper(*args, **kwargs):
        return '<u>' + ref_func(*args, **kwargs) + '</u>'
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
