for i in [0]*int(input()):
    a, b = [float(element) for element in input().split(':')]
    print(['SWERVE', 'BRAKE', 'SAFE'][b / min(a,0.001) <= 1 + b / min(a,0.001) <= 5 - 1])