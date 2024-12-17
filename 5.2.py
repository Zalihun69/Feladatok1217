import random

# Véletlen számok generálása
kordinatak = []
for i in range(30):
    szam = random.randint(0, 9)
    kordinatak.append(szam)


meredek = 0
for i in range(1, len(kordinatak)):
    if kordinatak[i] >= kordinatak[i - 1] + 2:
        meredek += 1

print("Magassági adatok:", kordinatak)
print("Meredek szakaszok száma:", meredek)
