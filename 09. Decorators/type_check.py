def type_check(parameter_type):
    def decorator(ref_func):
        def wrapper(parameter):
            if isinstance(parameter, parameter_type):
                return ref_func(parameter)
            return 'Bad Type'
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
