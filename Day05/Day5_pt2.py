    #DAY5
#PT2
from pathlib import Path
import re


fn = 'input.txt'
strings = []
stacks = []
rules = []
result = []


def Main():
    stack = Input()
    for rule in rules:
        rule = list(rule[0])
        rule = [int(p) for p in rule]
        temp_stack = []
        for i in range(0, rule[0]):
            temp_stack.append(stack[rule[1]-1].pop())
        temp_stack.reverse()
        for element in temp_stack:
            stack[rule[2]-1].append(element)
    for i in range(0,9): 
        stack[i].reverse()
        result.append(stack[i][0].strip("[ ]"))
    print(result)
    
    
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


def Input():
    p = Path(__file__).with_name(fn)
    with p.open('r') as fp:
        for l in fp:
            strings.append(l.strip('\n'))
    for i in range(0, 8):
        stacks.append( [ strings[i][j:j+4] for j in range(0, len(strings[i]), 4) ] )
    stack = list(zip(*stacks[::-1]))

    for i in range(0,9):
        stack[i] = remove_values_from_list(stack[i], '    ')
        stack[i] = remove_values_from_list(stack[i], '   ')

    for i, l in enumerate(strings):
        if (i>9):
            rules.append(re.findall('move (\d+) from (\d+) to (\d+)', l))
    return stack


if __name__ == '__main__':
    Main()