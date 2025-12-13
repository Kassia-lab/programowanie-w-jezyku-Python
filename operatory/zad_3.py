def czy_parzysta(liczba):
    return liczba % 2==0

wynik = czy_parzysta(7)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")