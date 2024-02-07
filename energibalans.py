Atemp = 79
Avagg = 69
Afonster = 16
Adorr = 2.1
Agrund = 40
Atak = 62
Aom = 189

Uvagg = 0.3
Ufonster = 1.1
Ugrund = 0.25
Utak = 0.25
Udorr = 1.1

Ktrans = ((Uvagg*Avagg) + (Ugrund*Agrund) + (Utak*Atak) + (Ufonster*Afonster) + (Udorr*Adorr)) * 1.1

Etrans = Ktrans * 98.600 / Atemp

Um = Ktrans/Aom


# E
# Beräkningar av värmeförlusterna från ventilationen och luftläckage

qvent = 0.35
pacpa = 1200

Ravent = qvent*Atemp/1000
Kvent = Ravent * pacpa
Event = Kvent * 98.600 / Atemp

q50=0.9
Ralack = 0.04 * q50 * Aom /1000
Klack = Ralack * pacpa
Elack = Klack * 98.600 / Atemp

#F

Efastighetsel = 3

# G

Epers = 14
Eel = 21
Esol = 35 * Afonster/Atemp
Etapp = 25 
Evadring = 4 

Euppv = Etrans + Event + Elack + Evadring - Epers - Eel - Esol
Ebea = Etrans + Event + Elack + Etapp + Evadring + Efastighetsel - Epers - Eel - Esol

# J

EPet = (Euppv/0.9+Etapp)*1+Efastighetsel*1.6

Y = (Ktrans + Kvent) * (21+1.2) - 500

Y2 = Y*12/1000

print(EPet)
print('Y=',Y)
print('Y2=',Y2)
print('Ebea=',Ebea)
print('Ktrans=', Ktrans)
print('Kvent=',Kvent)
print('Ravent=', Ravent)




