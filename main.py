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

nContains = str.lower(input("Should it contain numbers? y/n: "))
lContains = str.lower(input("Should it contain letters? y/n: "))
sContains = str.lower(input("Should it contain symbols? y/n: "))
power = int(input("Enter number of characters: "))
r = input('Generate? y/n: ')
u = [element.upper() for element in u]

while r == 'y':
    p = []
    p.append(str(''.join(u)))
    if nContains == "y":
        p.append(str(''.join(n)))
    if lContains == "y":
        p.append(str(''.join(letter)))
    if sContains == "y":
        p.append(str(''.join(s)))
    if len(p) == 0:
        print('You want an empty password :D')
    array = ''.join(p)
    passw = []
    for i in range(power):
        passw.append(choice(array))
    print("Your password is: >>>", ''.join(passw), '<<<')
    r = input('Re-generate? y/n: ')
print('Don`t forget to save your password!')
