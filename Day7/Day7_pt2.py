    #DAY7
#PT2
from pathlib import Path

fn = "input.txt"
NUM = 30000000
DEF = 70000000
input = []
dir = []
output = []
point = 0

class Directory(object):
    def __init__(self, name, data):
        self.data = data
        self.name = name
        self.children = []
        self.parent = None

    def add_child(self, obj):
        obj.parent = self
        self.children.append(obj)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def points(self):
        global point
        point += int(self.data)
        if self.children:
            for child in self.children:
                child.points()
        return point

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix, self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def search_result(self):
        global point
        point = 0
        if self.points()>=0:
            output.append(int(self.points()/2))
        point = 0
        if self.children:
            for child in self.children:
                child.search_result()


def Main():
    global point, NUM
    files = 0
    init = 1
    p = Path(__file__).with_name(fn)
    with p.open('r') as fp:
        for l in fp:
            l = l.strip().split(" ")
            if l[0] == "$":
                if l[1] == "cd":
                    if l[2]=="..":
                        act = act.parent
                    else:
                        if init == 1:
                            act = Directory(l[2], files)
                            files = 0
                            head = act
                            init = 0
                        elif act.children:
                            for child in act.children:
                                if l[2]==child.name:
                                   act = child
            elif l[0] == "dir":
                dir = Directory(l[1], files)
                act.add_child(dir)
            else:
                act.data += int(l[0])
    head.print_tree()
    head.search_result()
    output.sort(reverse=True)
    result = [item for item in output if NUM <= item + (DEF - output[0])]
    result.sort()
    print (result[0])

    
if __name__ == '__main__':
    Main()