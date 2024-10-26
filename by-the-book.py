test = lambda: sum(a * b for a, b in [(index, int({'X': 10}.get(char, char))) for index, char in enumerate(input())])
print('\n'.join(str(test()) for i in [0]*int(input())))