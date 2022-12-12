    #DAY10
#PT1
from pathlib import Path

fn = "input.txt"
cicles = [20, 60, 100, 140, 180, 220]
sign_strenght = 0
prev_cicle = 0

def Main():
    p = Path(__file__).with_name(fn)
    with p.open('r') as fp:
        cicles = fp.read().splitlines()

    cicle_count = 0
    x = 1

    for cicle in cicles:
        cicle = cicle.split(' ')
        cicle_count += 1
        sign_strenght = check_count(cicle_count, x)
        if cicle[0] == 'addx':
            sign_strenght = check_count(cicle_count, x)
            cicle_count += 1
            sign_strenght = check_count(cicle_count, x)
            x += int(cicle[1])
    print(sign_strenght)


def check_count(cicle_count, x):
    global cicles, sign_strenght, prev_cicle
    if prev_cicle == cicle_count:
        return sign_strenght
    elif cicle_count in cicles:
        prev_cicle = cicle_count
        sign_strenght += cicle_count*x
    return sign_strenght

if __name__ == '__main__':
    Main()
