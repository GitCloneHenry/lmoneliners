for i in [0]*int(input()):
    print(''.join(map(str, [letter for letter in input().lower() if letter in 'abcdefghijklmnopqrstuvwxyz|'])).split('|'))
    # print(((
    #     sum(a.count(letter) for letter in b) < len(b)) for a, b in ''.join(
    #         map(str, [letter for letter in input().lower() if letter in 'abcdefghijklmnopqrstuvwxyz'])).split('|')))
    # print('You\'re not a secret agent!' if ((sum(a.count(letter) for letter in b) < len(b)) for a, b in '\n'.join(map(str, [letter for letter in input().lower() if letter in 'abcdefghijklmnopqrstuvwxyz'])).split('|')) else 'That\'s my secret contact!')