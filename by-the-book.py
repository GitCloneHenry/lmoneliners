# [(lambda isbn : print('\n'.join(['INVALID', 'VALID'][{10: 'x'}.get(diff := abs((total := sum(a * b for a, b in [(index, int({'X': 10}.get(char, char))) for index, char in enumerate(isbn)])) - (-(-total // 11) * 11)), str(diff)) == isbn[-1]])))(input()) for i in [0]*int(input())]
[(lambda isbn : print(diff := abs((total := sum(a * b for a, b in [(index, int({'X': 10}.get(char, char))) for index, char in enumerate(isbn)])) - (-(-total // 11) * 11)) == isbn[-1]))(input()) for i in [0]*int(input())]