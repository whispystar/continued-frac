import math

#todo
#possibly a way to visualize the PSL_2(Z)

def gen_farey(n):
    seq = [(0,1),(1,1)]
    for i in range(0, n):
        newLayer = []
        for j in range(0, len(seq)-1):
            newLayer.append(seq[j])
            newLayer.append((seq[j][0] + seq[j+1][0], seq[j][1] + seq[j+1][1]))
        newLayer.append((1,1))
        seq = newLayer
    return seq

def gen_scf(n):
    seq = []

    if n[0] < n[1]:
        seq.append((0,0))

        num = n[0]
        den = n[1]
    else:
        num = n[1]
        den = n[0]

    while num != 1:
        tmp = num
        num = den
        den = tmp

        a = math.floor(num / den)
        seq.append((a,0))
        num = num - (a * den)
    seq.append((den,0))

    return seq

def gen_nicf(n):
    seq = []

    if n[0] < n[1]:
        seq.append((0, 0))

        num = n[0]
        den = n[1]
    else:
        num = n[1]
        den = n[0]

    while num != 1:
        tmp = num
        num = den
        den = tmp

        a_floor = math.floor(num / den)
        a_ceil = math.ceil(num / den)

        if abs((a_floor * den) - num) <= abs((a_ceil * den) - num):
            seq.append((a_floor, 0))
            num = num - (a_floor * den)
        else:
            seq.append((a_ceil, 1))
            num = (a_ceil * den) - num
    seq.append((den, 0))

    return seq

def seq_to_frac(seq):
    seq.reverse()

    num = 1
    den = seq[0][0]

    for i in range(1, len(seq)):
        if seq[i][1] == 0:
            tmp = den
            den = (den * seq[i][0]) + num
            num = tmp
        else:
            tmp = den
            den = (den * seq[i][0]) - num
            num = tmp

    return (den, num)

def gen_convergents(seq):
    convergents = []
    for i in range(1, len(seq)+1):
        convergents.append(seq_to_frac(seq[:i]))
    return convergents

farey_sequence = gen_farey(15)[1:-1]

for frac in farey_sequence:
    scf = gen_scf(frac)
    nicf = gen_nicf(frac)

    if len(scf) != len(nicf):
        scf_convergents = gen_convergents(scf)
        nicf_convergents = gen_convergents(nicf)

        print(frac)
        print(scf_convergents)
        print(nicf_convergents)

