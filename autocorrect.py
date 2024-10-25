compare_strings = lambda a, b: sum(1 for a, b in zip(a, b) if a != b) + abs(len(a) - len(b))

for i in [0]*int(input()):
    a, b = list(map(int, input().split(' ')))

    words = [input() for j in [0]*a]

    compared = [compare_strings(input(), word) for word in words]
    print('\n'.join(words[compared.index(min(compared))]))
