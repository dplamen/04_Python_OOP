class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.end = self.step * (self.count - 1)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        n = self.start
        self.start += self.step
        return n


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
