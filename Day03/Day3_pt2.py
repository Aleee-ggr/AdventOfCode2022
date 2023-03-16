    #DAY3
#PT2
from pathlib import Path

fn = 'input_complete.txt'
points = 0
strings = []
group = []
items = []

def Main():
    Input()
    for string in strings:
        group.append(string)
        if len(group)==3:
            CheckChar()
            Scoring()
    print(points)


def Input():
    p = Path(__file__).with_name(fn)
    with p.open('r') as fp:
        for l in fp:
            strings.append(l.strip())


def CheckChar():
    for char in group[0]:
        if char in group[1] and char in group[2]:
            items.append(char)
            group.clear()
            break


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