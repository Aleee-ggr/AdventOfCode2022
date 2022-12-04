    #DAY4
#PT2
from pathlib import Path
import re

fn = 'input.txt'
strings = []
items = []

def Main(data):
    result = 0
    pairs = re.findall('(\d+)-(\d+),(\d+)-(\d+)', data)
    for pair in pairs:
        pair = [int(p) for p in pair]
        if(Overlap(pair)):
            result+=1
    print(result)

    
def Overlap(a):
    return( a[0]<=a[2]<=a[1] or a[2]<=a[1]<=a[3] or 
            a[2]<=a[0]<=a[3] or a[0]<=a[3]<=a[1])


if __name__ == '__main__':
    p = Path(__file__).with_name(fn)
    with p.open('r') as fp:
        data = fp.read()
    Main(data)