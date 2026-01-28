import math, random
from fractions import Fraction

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

def gen_nscf(n):
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

        a = math.ceil(num / den)
        seq.append((a,1))
        num = (a * den) - num
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

def frac_diff(f1, f2):
    num = f2[0]*f1[1] - f1[0]*f2[1] 
    den = f1[1]*f2[1]

    divisor = math.gcd(num, den)
    return (num//divisor, den//divisor)

def latex(cf):
    cmd ="\\nicf{"
    cmd = cmd + str(cf[0][0]) + '}{'

    for i in cf[1:]:

        if i[1] == 0:
            cmd = cmd + str(1) +'/' + str(i[0]) +','
        elif i[1] ==1 : 
            cmd = cmd + '-' + str(1) +'/' + str(i[0]) +','
    
    return cmd[0:-1] + '}'

'''
frac = (50,127)
print(frac)
print("SCF: ", end="")
print(gen_scf(frac))
convergents = gen_convergents(gen_scf(frac))

#for i in range(0, len(convergents)-1):
#    print(frac_diff(convergents[i], convergents[i+1]))
print(convergents)
#for con in convergents:
#    if con != (0,1):
#        print(con)
#        print(gen_scf(con))
#        print(gen_nicf(con))
print("NICF: ", end="")
print(gen_nicf(frac))
print(gen_convergents(gen_nicf(frac)))
print()

'''

farey_seq = gen_farey(10)[1:-1]

for i in range(0, 10):
    frac = farey_seq[random.randint(0,len(farey_seq))]
    #frac = (143147,496350)
    scf_con = gen_convergents(gen_scf(frac))
    nscf_con = gen_convergents(gen_nscf(frac))
    nicf_con = gen_convergents(gen_nicf(frac))
    print(frac)
    print("SCF: ", end="")
    print(gen_scf(frac))
    print("LaTeX: ", end='') 
    print(latex(gen_scf(frac)))
    print("Convergents: ", end="")
    print(scf_con)

    scf_con_diff = []
    for i in range(0, len(scf_con)-1):
        scf_con_diff.append(frac_diff(scf_con[i], scf_con[i+1]))
    print(scf_con_diff)
    print("NICF: ", end="")
    print(gen_nicf(frac))
    print("LaTeX: ", end='') 
    print(latex(gen_nicf(frac)))
    print("Convergents: ", end="")
    print(nicf_con)

    nicf_con_diff = []
    for i in range(0, len(nicf_con)-1):
        nicf_con_diff.append(frac_diff(nicf_con[i], nicf_con[i+1]))
    print(nicf_con_diff)

    print("NSCF: ", end = "")
    print(gen_nscf(frac))
    print("LaTeX: ", end='') 
    print(latex(gen_nscf(frac)))
    print("Convergents: ", end="")
    print(nscf_con)
    print()

