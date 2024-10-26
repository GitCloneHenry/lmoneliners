test = lambda: sum(a * int(b) if b != 'X' else a * 10 for a, b in enumerate(input().split()))
print('\n'.join(test() for i in [0]*int(input())))