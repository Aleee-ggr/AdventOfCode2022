    #DAY12
#PT1
import numpy as np
from pathlib import Path


fn = "input.txt"

def Input():
    p = Path(__file__).with_name(fn)
    with p.open('r') as fp:
        matrix = np.loadtxt(fp, dtype=np.unicode_)
        

def Main():
    Input()


if __name__ == '__main__':
    Main()
