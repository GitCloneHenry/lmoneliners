test = lambda: sum(a * b for a, b in [{'X': 10}.get(char, int(char)) for char in input()])
print('\n'.join(test() for i in [0]*int(input())))