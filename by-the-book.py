[(lambda isbn : print(['INVALID', 'VALID'][{10: 'x'}.get(diff := -(total := sum((10 - a) * b for a, b in [(index, int({'X': 10}.get(char, char))) for index, char in enumerate(isbn)]) + (-total // 11) * 11), str(diff)) in ['0', isbn[-1]]]))(input()) for i in [0]*int(input())]