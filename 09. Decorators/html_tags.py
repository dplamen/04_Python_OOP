def tags(tag):
    def decorator(ref_func):
        def wrapper(*args):
            return f'<{tag}>{ref_func(*args)}</{tag}>'
        return wrapper
    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
