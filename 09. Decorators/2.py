def vowel_filter(function):
    def wrapper():
        letters = function()
        return [l for l in letters if l.lower() in 'aoueiy']
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())

