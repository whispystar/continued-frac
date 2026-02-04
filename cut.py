import math
from fractions import Fraction

def scf(cut):
    confrac =[]
    for i in cut:
        confrac.append((i,0))

    return confrac

def cut_to_num(scf):
    if len(scf) == 1:
        return scf[0]
    else:
        try:
            return scf[0] * cut_to_num(scf[1:])+cut_to_num(scf[2:])
        except IndexError:
            return scf[0] +1
        
def cut_to_den(scf):
    return cut_to_num(scf[1:])

for i in range(10):
    cut = [1,4,i]
    try:
        if cut_to_num(cut[1:]) / cut_to_den(cut[:1]) <= cut[0]*1/2:
            print('continue')
        else:
            print('ROUND: ', str(cut))
            break
    except IndexError:
        print('test')