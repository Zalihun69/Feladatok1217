
mondatok = []
for i in range(5):
    mondat = input(f"Kérem adja meg a(z) {i+1}. mondatot: ")
    mondatok.append(mondat)


max_szokoz = -1
leg_tobb_szokoz_mondat = ""


for mondat in mondatok:
    szokozok_szama = 0
    for karakter in mondat:
        if karakter == ' ':
            szokozok_szama += 1
    
    if szokozok_szama > max_szokoz:
        max_szokoz = szokozok_szama
        leg_tobb_szokoz_mondat = mondat


print("A legtöbb szóközt tartalmazó mondat:")
print(leg_tobb_szokoz_mondat)