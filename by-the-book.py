test = lambda: sum(a * b for a, b in [(index, {'X': 10}.get(char, int(char))) for index, char in enumerate(input())])
print('\n'.join(test() for i in [0]*int(input())))