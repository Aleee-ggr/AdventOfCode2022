    #DAY10
#PT2
from pathlib import Path

fn = "input.txt"
cicles = [40, 80, 120, 160, 200, 240]
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
        sign_strenght = check_count(cicle_count, x)
        cicle_count += 1
        sign_strenght = check_count(cicle_count, x)
        if cicle[0] == 'addx':
            sign_strenght = check_count(cicle_count, x)
            cicle_count += 1
            sign_strenght = check_count(cicle_count, x)
            x += int(cicle[1])
    print(sign_strenght)


def check_count(cicle_count, x):            #bad lazy code
    global cicles, sign_strenght, prev_cicle
    if prev_cicle == cicle_count:
        return sign_strenght
    if cicle_count in cicles:
        prev_cicle = cicle_count
        print("\n")
    else:
        if x-1 <= cicle_count%40 <= x+1:
            print("#", end='')
        else:
            print(".", end='')
    return sign_strenght


if __name__ == '__main__':
    Main()