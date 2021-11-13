def squares(n):
    num = 1
    while num <= n:
        yield num ** 2
        num += 1


class squares_iter:
    def __init__(self, n):
        self.end = n
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        temp = self.start
        self.start += 1
        return temp**2


print(list(squares(5)))
print(list(squares_iter(5)))