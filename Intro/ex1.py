# Zmienne:

# int - liczba całkowita
# float - liczba z przecinkiem 
# bool - zmienna logiczna 
# string - łańuch znaków

"""

x = 10  # int x = 5 -- definiowanie zmiennej typu integer
y = 1.5 
z = "cześć"

# Jak wypisać wszystkie zmienne na ekran 

print (x,y,z)

# jak pobrać zmienne od uytkownika 

a = input() #kazda liczba, którą podajesz z klawiatury jest traktowana jako string 
print(a + "12") #operacja konkatenacji - połączenie dwóch stringów

# Jak zrobic aby program rozpoznawał zmienne 
# rzutowanie typu 

a = int(input())
f = float(input())
s = str(input()) # s = input()
# uztkownik podaje - nazwe produktu, cene jednej sztuki, liczba sztuk -- obliczamy całkowity koszt 

nazwa_produktu = str(input())
cena_jednej_sztuki = float(input())
liczba_sztuk = int(input())

print("nazwa produktu to:", nazwa_produktu, "a całkowity koszt wynosi:", cena_jednej_sztuki * liczba_sztuk)

x = int(input())
if x < 0:
    print(x*-1)
else:
    print(x)


x = int(input())
if x > 10:
    print(x)
else:
    print(x%3)


wiek = int(input())
if wiek < 0:
    print("nie można mieć -1 lat")
else:
    if wiek < 12:
        print("dziecko")
    elif wiek > 12 and wiek < 18:                 # and - && or - || 
        print ("nastolatek")
    elif wiek >= 18 and wiek <= 25:
        print ("młody dorosły")
    elif wiek > 25 and wiek < 65:
        print ("dorosły")
    else:
        print("senior")


# for i in range(od, do, co ile)


# jak zsumowac liczby od 1 do 100 

"""

suma = 0 # zmienna globalna dla pętli for 
for i in range (1,101,1):
    suma = suma + i

print(suma)

# sume liczb od 1 do 1000 ale tylko podzielne przez 2 i 3 

suma = 0
for i in range (1 , 1001, 1):
    if i % 2 == 0 and i % 3 == 0:
        suma = suma + i
print(suma)

x = int(input())
suma = 0
for i in range (1,x+1,1):
    if x % i == 0:
        suma = suma + i
print(suma)


# Typy złozone:
#Struktury danych do przechowywania wartosci 
# Lista(tablica) [], modyfikowalna

A = ["kasia", "basia", "ania"] #indeksy 0 1 2 ... 
print(A[1]) # wypisuje basie 
print(A[2]) # wypisze ania 
print(A[3]) # Index out of range --- błąd !!! 
A.append("zosia")
A.pop("kasia")


# krotka (), niemodyfikowalna -- wspołrzedna

wsp = (12.2,11.4,80.3)


# słownik {} key: value 

uczen = {

    "imie": "Anna",
    "wiek": 17,
    "klasa": "3A",
    "srednia": 4.5
}
print(uczen["imie"]) # ania 
print(uczen["srednia"]) #4.5

# słownik uczen to nie to samo co Uczen 


A = ["kasia", "basia", "ania"]


for i in range (0,len(A),1):
    print(A[i])

# dla zmiennych złozonych - for-each 

for imie in A:
    print(imie)

