def possible_permutations(seq):
    perms = all_permutations(seq)
    for perm in perms:
        yield perm


def all_permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        n = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in all_permutations(remLst):
            l.append([n] + p)
    return l


[print(n) for n in possible_permutations([1, 2, 3])]
