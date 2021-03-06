kosar = {}
vasarlasok = []

with open('penztar.txt') as file:
    for line in file:
        line = line.strip()
        if line == 'F':
            vasarlasok.append(kosar)
            kosar = {}
        else:
            if line in kosar:
                kosar[line] += 1
            else:
                kosar[line] = 1
print('2. feladat')
print(f'A fizetések száma: {len(vasarlasok)}')

print('3. feladat')
print(f'Az első vásárló {len(vasarlasok[0])} darab árucikket vásárolt.')

print('4. feladat')
sorszam = 2 - 1#int(input('Adja meg egy vásárlás sorszámát! ')) - 1
nev = 'kefe' #input('Adja meg egy árucikk nevét! ')
db = 2 #int(input('Adja meg a vásárolt darabszámot! '))

print('5. feladat')
vasarolt = False
osszesen = 0
utolso_vasarlas = 0
for index, kosar in enumerate(vasarlasok):
    for arucikk in kosar:
        if arucikk == nev and not vasarolt:
            print(f'Az első vásárlás sorszáma: {index + 1}')
            vasarolt = True
        if arucikk == nev:
            utolso_vasarlas = index + 1
            osszesen += 1
print(f'Az utolsó vásárlás sorszáma: {utolso_vasarlas}')
print(f'{osszesen} vásárlás során vettek belőle.')

def ertek(db):
    if db == 1:
        return 500
    elif db == 2:
        return 950
    else:
        return 950 + (db - 2) * 400

print('6. feladat')     
print(f'{db} darab vételekor fizetendő: {ertek(db)}')

print('7. feladat')
for item in vasarlasok[sorszam]:
    print(f'{vasarlasok[sorszam][item]} {item}')