from statistics import mean; [(lambda a: (lambda in_data: print(f"{a[0]}={0 if not in_data else mean(in_data):.3f}"))([['K', '1B', '2B', '3B', 'HR'].index(hit) for hit in a[1].split(",") if not hit in ['BB', '']]))([i for i in input().split(':')]) for i in [0]*int(input())]