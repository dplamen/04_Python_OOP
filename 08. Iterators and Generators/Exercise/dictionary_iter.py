class dictionary_iter:
    def __init__(self, kwargs):
        self.kwargs = kwargs

    def __iter__(self):
        self

    def __next__(self):
        pass


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
