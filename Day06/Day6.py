    #DAY6
#PT1 #PT2
#solution 1 - > NUM = 4
#solution 2 - > NUM = 14
from pathlib import Path
from collections import Counter

fn = "input.txt"
buffer = []
NUM = 14 

p = Path(__file__).with_name(fn)
with p.open('r') as fp:
    data = fp.read()

for i, char in enumerate(data):
    if len(buffer)<NUM:
        buffer.append(char)
    else:
        c = Counter(buffer)
        if len(list(c))==NUM:
            print(list(c), c)
            print(i)
            break
        buffer.reverse()
        buffer.pop(NUM-1)
        buffer.reverse()
        buffer.append(char)