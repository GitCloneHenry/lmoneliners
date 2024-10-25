for i in [0]*int(input()):
    name, hits = list(map(lambda str : str.split(','), input().split(':')))

    percentage = sum(['K', '1B', '2B', '3B', 'HR'].index(hit) for hit in hits)
    print(f"{name}={0 if not percentage else percentage / len(hits)}")