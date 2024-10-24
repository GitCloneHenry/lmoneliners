print('\n'.join("You're not a secret agent!" if ((lambda str : sum(str[0].count(char) > 0 for char in str[1]) < len(str[1]))(''.join(c for c in input().lower() if c.isalpha() or c == '|').split('|'))) else 'That\'s my secret contact!' for i in [0]*int(input())))

    