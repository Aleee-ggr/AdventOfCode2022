#bad code
from pathlib import Path

fn = 'input.txt'
strings = []
items = []

def Main():
    result = 0
    Input()
    for pairs in strings:
        pairs[0] = pairs[0].split('-')
        pairs[1] = pairs[1].split('-')
        pairs[0] = [int(x) for x in pairs[0]]
        pairs[1] = [int(x) for x in pairs[1]]
        if(Overlap(pairs[0], pairs[1])):
            result+=1
    print(result)
    
def Overlap(a, b):
    return(a[1]>=b[1] and a[0]<=b[0]) or (b[1]>=a[1] and b[0]<=a[0])

def Input():
    p = Path(__file__).with_name(fn)
    with p.open('r') as fp:
        for l in fp:
            strings.append(l.strip().split(','))



if __name__ == '__main__':
    Main()