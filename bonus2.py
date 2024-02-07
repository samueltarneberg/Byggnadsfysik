# UPG 1

T1 = 23
T2 = -7
d1 = 0.264
d2 = 0.236
d3 = 0.015
l1 = 1.7
l2 = 0.04
l3 = 0.14

Rse=0.04
Rsi=0.13
R1 = d1/l1
R2 = d2/l2
R3 = d3/l3
Rtot = R1+R2+R3 + Rse + Rsi

T = T1 - ((Rsi/Rtot)*(T1-T2))

print(T)

#UPG 2
dg = 0.2336
lg = 3.5

dm = 0.160
lm = 0.04


Rg = dg/lg
Rm = dm/lm

U = 1 / (Rg + Rm + Rse + Rsi)

print(U)

#UPG 3
Ktot = 43 + 29 + 23

Q = Ktot * ( 19 + 19)

print(Q)



