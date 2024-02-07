import numpy as np 

#Upg 1
V = 6*0.25*2.6
dT = 1.5
rho = 2300
C_p = 900 
Q = (C_p * rho * V * dT)/3600000

print('Q=', Q)

#UPG 2
I0 = 479
alpha_ks = 0.9
Tu=9
Ks=65
Kk=196
A=10

Te = ((Tu*Kk) + (Tu*Ks) + (I0*alpha_ks))/(Kk+Ks)

print('Te=', Te)

#UPG 3
#För att minska värmeförlusterna förses ett 2-glasfönster med lågemissionskikt. Emissionstalet på glasens insidor är 0,24 och värmeöverföringskoefficienten för ledning och konvektion i spalten mellan glasen antas vara 1,7 W/m2K. Innetemperaturen är 22 
#C och utetemperaturen är 7 
#C. Beräkna värmeflödet, W/m2, genom fönstret.
# SVAR: 25.8
Tute = 7
Tinne = 22
alpkl = 1.7
sigma = 5.67 * 10**(-8)
es = (1/((2/0.24)-1))
alps = ((4*sigma*(287.5)**3)/(2*((1-0.24)/0.24)+1))


rtot=0.04 + 0.13 +1/(alpkl + alps)

q = (Tinne - Tute)* 1/(0.04 + 0.13 +1/(alpkl + alps))

print('q=',q)


#UPG 5
T1 = 273 + 73
T2 = 273 + 22
e1 = 0.97
e2 = 0.78
A1 = 0.8
A2 = 45
Tm = (T1+T2)/2 


alp = (4 * sigma * Tm**3)/(((1-e1)/e1) + 1 + A1/A2*(1-e2)/e2)

Q12 = alp * A1 *(T1-T2)


print('Q12=', Q12)