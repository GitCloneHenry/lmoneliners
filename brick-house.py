print('\n'.join(['false', 'true'][(c - a) // 5 <= b] for a, b, c in (list(map(int, input().split())) for i in [0]*int(input()))))