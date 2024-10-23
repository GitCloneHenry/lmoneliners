for i in [0]*int(input()):
    a, b = [float(element) for element in input().split(':')]
    print(['SWERVE', 'BRAKE', 'SAFE'][(b <= a) + (b <= 5 * a) - 1])