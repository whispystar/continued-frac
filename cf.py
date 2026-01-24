import math

#todo
#go backwards ( sequence to rational )
#possibly a way to visualize the PSL_2(Z)

def gen_farey_0_to_1(n):
    seq = set()
    if n < 2:
        return seq
    for denominator in range(2, n+1):
        for numerator in range(1, denominator):
            gcd = math.gcd(numerator, denominator)
            seq.add((numerator//gcd, denominator//gcd))

    return list(seq)

def gen_farey_natural(n):
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
        seq.append(0)

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
        seq.append(a)
        num = num - (a * den)

    seq.append(den)

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

def nicf_to_frac(seq):
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

def scf_to_frac(seq):
    seq.reverse()

    num = 1
    den = seq[0]

    for i in range(1, len(seq)):
        tmp = den
        den = (den * seq[i]) + num
        num = tmp

    return (den, num)


#MAIN

farey_seq = gen_farey_natural(15)[1:-1]

for fraction in farey_seq:
    scf = gen_scf(fraction)
    nicf = gen_nicf(fraction)
    print(fraction, scf, nicf, len(scf), len(nicf))


