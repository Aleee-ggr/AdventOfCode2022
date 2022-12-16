    #DAY11
#PT1 #PT2
from pathlib import Path
from math import gcd
import operator

fn = "input.txt"
DIVISOR = 3
ROUND_NUM = 10000
PART_1 = False
PART_2 = True


ops = {
    '+' : operator.add,
    '*' : operator.mul,
}

class Monkey:
    def __init__(self, data):
        self.data = data
        self.op = None
        self.new = None
        self.test_div = None
        self.true = None
        self.false = None
        self.number = 0
        self.items = []        


monkeys = []
time_inspect = []
divs = []
modules = 0


def Input():
    global divs, modules
    p = Path(__file__).with_name(fn)
    with p.open('r') as fp:
        elements = fp.read().replace(',',"").split("\n\n")
        elements = [element.strip().split("\n") for element in elements]
        elements = [[e.strip().split(' ') for e in element] for element in elements]
        [monkeys.append(Monkey(element)) for element in elements]
        for monkey in monkeys:
            monkey.items = monkey.data[1][2:]
            monkey.op = monkey.data[2][4]
            if monkey.data[2][5] == 'old':
                monkey.new = monkey.data[2][5]
            else:
                monkey.new = int(monkey.data[2][5])
            monkey.test_div = int(monkey.data[3][3])
            divs.append(int(monkey.data[3][3]))
            monkey.true = int(monkey.data[4][5])
            monkey.false = int(monkey.data[5][5])
    if PART_2:
        modules = lcm(divs)


def lcm(list):
    l = 1
    for i in list:
        l = l*i//gcd(l,i)
    print (l)
    return l


def Main():
    global modules, DIVISOR, ROUND_NUM, PART_1, PART_2
    Input()
    for i in range(0, ROUND_NUM):
        for monkey in monkeys:
            items_buffer = list(monkey.items)
            for count,item in enumerate(items_buffer):
                if(monkey.new == 'old'):
                    worry = ops[monkey.op](int(item), int(item))
                else:
                    worry = ops[monkey.op](int(item), int(monkey.new))
                if(PART_1):
                    worry = int(worry/DIVISOR)
                if(PART_2):
                    worry = worry % modules
                if(worry % monkey.test_div):
                    monkeys[monkey.false].items.append(worry)
                    monkey.items.remove(item)
                else:
                    monkeys[monkey.true].items.append(worry)
                    monkey.items.remove(item)
            monkey.number += (count+1)
        print(i)
    for monkey in monkeys:
        time_inspect.append(monkey.number)
    time_inspect.sort(reverse = True)
    print(time_inspect)
    print(time_inspect[0]*time_inspect[1])


if __name__ == '__main__':
    Main()
