    #DAY1
#PT1
from pathlib import Path

fn = 'input.txt'
tot = 0
result = []
p = Path(__file__).with_name(fn)

with p.open('r') as fp:
    for l in fp:
        if l==' ' or l=='\n':
            result.append(tot)
            tot = 0
        else:
            tot += int(l) 
    result.append(tot)

result.sort(reverse=True)
print(result[0])
