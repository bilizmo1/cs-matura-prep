# ZADANIE 1
# Napisz program, który pobiera od użytkownika nazwę produktu,
# cenę jednej sztuki oraz liczbę zakupionych sztuk.
# Oblicz całkowity koszt zakupów.
# Jeżeli koszt przekracza 100 zł, zastosuj rabat 10%.
# Wyświetl nazwę produktu i końcową kwotę do zapłaty.


# ZADANIE 2
# Napisz program, który pobiera od użytkownika trzy oceny.
# Oblicz ich średnią arytmetyczną.
# Następnie wyświetl odpowiedni komunikat:
# średnia < 2.0        -> "Musisz poprawić oceny"
# 2.0 <= średnia < 3.5 -> "Wynik dostateczny"
# 3.5 <= średnia < 4.5 -> "Dobry wynik"
# średnia >= 4.5       -> "Świetny wynik!"


# ZADANIE 3
# Napisz program, który pobiera dodatnią liczbę całkowitą n.
# Oblicz sumę wszystkich liczb od 1 do n,
# które są podzielne przez 3, ale nie są podzielne przez 5.
# Nie używaj funkcji sum().
# Przykład: n = 15, wynik = 30.


# ZADANIE 4
# Napisz program, który pobiera dodatnią liczbę całkowitą n.
# Wypisz wszystkie dzielniki tej liczby.
# Następnie policz, ile dzielników ma ta liczba,
# oraz oblicz sumę wszystkich jej dzielników.
# Przykład: n = 12
# Dzielniki: 1, 2, 3, 4, 6, 12
# Liczba dzielników: 6
# Suma dzielników: 28


# ZADANIE 5
# Napisz program, który pobiera od użytkownika 8 liczb całkowitych.
# Wykorzystując pętlę for:
# - policz liczby parzyste,
# - policz liczby nieparzyste,
# - oblicz sumę liczb parzystych,
# - oblicz sumę liczb nieparzystych.
# Wyświetl wszystkie cztery wyniki.


# ZADANIE 6
# Utwórz listę:
imiona = ["Anna", "Kasia", "Ola", "Basia"]

# Napisz program, który:
# - wyświetli wszystkie imiona za pomocą pętli for,
# - doda do listy imię "Zosia",
# - usunie z listy imię "Kasia",
# - wyświetli liczbę elementów listy,
# - wyświetli wszystkie imiona wraz z ich indeksami.
# Wykorzystaj append(), pop(), len() i range().


# ZADANIE 7
# Utwórz pustą listę.
# Pobierz od użytkownika 6 liczb całkowitych i dodaj je do listy.
# Następnie:
# - wyświetl wszystkie liczby,
# - znajdź największą liczbę,
# - znajdź najmniejszą liczbę,
# - oblicz różnicę między największą a najmniejszą.
# Nie używaj funkcji max() ani min().
# Wykorzystaj pętlę for i instrukcje if.


# ZADANIE 8
# Pobierz od użytkownika dwie liczby x oraz y.
# Zapisz je w krotce punkt = (x, y).
# Sprawdź, w której ćwiartce układu współrzędnych
# znajduje się punkt:
# I ćwiartka: x > 0 i y > 0
# II ćwiartka: x < 0 i y > 0
# III ćwiartka: x < 0 i y < 0
# IV ćwiartka: x > 0 i y < 0
# Jeżeli x == 0 lub y == 0, sprawdź, czy punkt leży
# na osi OX, osi OY, czy w początku układu współrzędnych.


# ZADANIE 9
# Utwórz słownik:
uczen = {
    "imie": "Anna",
    "wiek": 17,
    "klasa": "3A",
    "srednia": 4.5
}

# Napisz program, który:
# - wyświetli imię ucznia,
# - wyświetli jego wiek,
# - zwiększy wiek o 1,
# - zmieni średnią ocen na 4.8,
# - doda nowy klucz "miasto" z wartością "Kraków",
# - wyświetli wszystkie klucze i wartości słownika.


# ZADANIE 10
# Napisz program symulujący prosty sklep internetowy.

produkty = [
    {"nazwa": "Chleb", "cena": 5},
    {"nazwa": "Mleko", "cena": 4},
    {"nazwa": "Maslo", "cena": 8},
    {"nazwa": "Jajka", "cena": 12}
]

# Program powinien:
# - wyświetlić wszystkie produkty wraz z cenami,
# - obliczyć sumę cen wszystkich produktów,
# - znaleźć najdroższy produkt,
# - policzyć, ile produktów kosztuje więcej niż 6 zł,
# - zastosować rabat 15%, jeżeli suma przekracza 25 zł,
# - wyświetlić końcową kwotę do zapłaty.
#
# Nie używaj funkcji sum() ani max().
# Wykorzystaj listy, słowniki, pętle for oraz instrukcje if.