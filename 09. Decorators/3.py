def even_numbers(function):
    def wrapper(numbers):
        x_arr = function(numbers)
        x_arr = [x for x in x_arr if x % 2 == 0]
        return x_arr
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
