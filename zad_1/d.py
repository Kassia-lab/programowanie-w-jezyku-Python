def wyswietl_co_drugi(lista_liczb):
    for i in range(0, len(lista_liczb), 2):
        print(lista_liczb[i])


# Przykład:
liczby = list(range(1, 11))
wyswietl_co_drugi(liczby)
