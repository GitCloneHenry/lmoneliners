print('\n'.join(
    str(
        sorted(
            point for point in (list(map(float, input().split(' '))) for j in [0]*int(input()))), 
            key=lambda point : (point[0] ** 2 + point[1] ** 2) ** 0.5) for i in [0]*int(input())))