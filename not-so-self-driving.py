for i in [0]*int(input()):
    a, b = [float(element) for element in input().split(':')]
    print(['SWERVE', 'BRAKE', 'SAFE'][b / a <= 1 + b / a <= 5 - 1])