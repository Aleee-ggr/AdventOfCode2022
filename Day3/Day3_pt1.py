    #DAY3
#PT1
from pathlib import Path

fn = 'input_complete.txt'
points = 0
strings = []
items = []

def Main():
    Input()
    for string in strings:
        first, second = string[:len(string)//2], string[len(string)//2:]
        for char in first:
            if char in second and char not in items:
                items.append(char)
        Scoring()
    print(points)


def Input():
    p = Path(__file__).with_name(fn)
    with p.open('r') as fp:
        for l in fp:
            strings.append(l.strip())


def Scoring():
    global points
    for item in items:
        if item.isupper():
            score = ord(item)-ord('A')+27
        if item.islower():
            score = ord(item)-ord('a')+1
        points += score
        items.clear()


if __name__ == '__main__':
    Main()