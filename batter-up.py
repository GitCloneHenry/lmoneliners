for i in [0]*int(input()):
    name, hits = list(map(lambda str : str.split(','), input().split(':')))

    percentage = [list(['K', '1B', '2B', '3B', 'HR']).index(hit) for hit in hits if hit != 'BB']
    print(f"{name[0]}={'0.000' if not len(percentage) else (lambda number: int(number * 1000 + 1) * 0.001 if (number * 1000 - int(number * 1000) >= 0.5) else round(number, 3))(sum(percentage) / len(percentage)):.3f}")
