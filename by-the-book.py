test = lambda: sum(a * 10 if b == 'X' else a * int(b) for a, b in enumerate(input().split()))
print('\n'.join(test() for i in [0]*int(input())))