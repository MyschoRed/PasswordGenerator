from random import choice

n = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]
letter = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]
s = [
    '!',
    '@',
    '#',
    '$',
    '%',
    '&',
    '*',
    '_',
    '.',
    '?',
]
u = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    '',
    'm',
    'n',
    'o',
    'p',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]

nContains = str.lower(input("Má heslo obsahovať čísla? a/n: "))
lContains = str.lower(input("Má heslo obsahovať písmena? a/n: "))
sContains = str.lower(input("Má heslo obsahovať znaky? a/n: "))
power = int(input("Zadaj počet znakov v hesle: "))
r = input('Vygenerovat? a/n: ')
u = [element.upper() for element in u]

while r == 'a':
    p = []
    p.append(str(''.join(u)))
    if nContains == "a":
        p.append(str(''.join(n)))
    if lContains == "a":
        p.append(str(''.join(letter)))
    if sContains == "a":
        p.append(str(''.join(s)))
    if len(p) == 0:
        print('Chces prazdne heslo :D')
    array = ''.join(p)
    passw = []
    for i in range(power):
        passw.append(choice(array))
    print("Nové náhodné heslo je: >>>", ''.join(passw), '<<<')
    r = input('Vygenerovat znova? a/n: ')
print('Nezabudni si heslo uložiť!')
