for i in [0]*int(input()):
    # print('\n'.join([f"{a} {b}" for a, b in sorted([map(int, input().split(' ')) for j in [0]*int(input())], key=lambda a, b: (a**2 + b**2)**0.5)]))
    print(sorted([list(map(int, input().split(' '))) for j in [0]*int(input())], key=lambda a, b: (a**2 + b**2)**0.5))