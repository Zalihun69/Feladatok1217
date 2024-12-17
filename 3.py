import random
nagyobb=[]
szamok=[]
nullától_kisebb=0
nullatol_nagyobb=0
for i in range(100):
    szam=(random.randint(-100,100))
    szamok.append(szam)
    if szam < 0:
        nullától_kisebb +=1
    elif szam > 0:
        nullatol_nagyobb +=1
for szam in szamok:
    if szam>50:
        nagyobb.append(szam)
        break

print(szamok)
print(nullatol_nagyobb)
print(nullától_kisebb)
print(nagyobb)



