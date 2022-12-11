    #DAY9
#PT1 #PT2
from pathlib import Path

fn = "input.txt"


def Main():
    p = Path(__file__).with_name(fn)
    with p.open('r') as fp:
        directions = fp.read().splitlines()
    
    head = [0, 0]
    tail = [0, 0]
    tails = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    visited = set()
    visited2 = set()

    for direction in directions:
        direction = direction.split(' ')
        for _ in range(0, int(direction[1])):
            head = [x + y for x, y in zip(head, move_set(direction[0]))]
            tail = tail_movements(tail, head)
            visited.add(tuple(tail))

            prev_tail = tail
            for i, t in enumerate(tails):
                t = tail_movements(t, prev_tail)
                prev_tail = t
                if i==7:
                    visited2.add(tuple(t))
        
    print("pt1: ",len(visited))
    print("pt2: ",len(visited2))
        

def move_set(line):
    match line:
        case 'L':
            return[-1, 0]
        case 'R':
            return[1, 0]
        case 'D':
            return[0, -1]
        case 'U':
            return[0, 1]
        case _:
            exit(-1)


def tail_movements(tail, head):
    delta = [x-y for x,y in zip(head, tail)]
    if abs(delta[0])>1 or abs(delta[1])>1:
        tail[:]=[n+(1 if dn>=1 else -1 if dn<=-1 else 0) for n, dn in zip(tail, delta)]
    return tail


if __name__ == '__main__':
    Main()