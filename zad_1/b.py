def podwoj_for(lista_liczb):
    nowa_lista = []
    for liczba in lista_liczb:
        nowa_lista.append(liczba * 2)
    return nowa_lista


# Przykład:
liczby = [1, 2, 3, 4, 5]


print(podwoj_for(liczby))


def podwoj_lista_skladana(lista_liczb):
    return [liczba * 2 for liczba in lista_liczb]


# Przykład:
liczby = [1, 2, 3, 4, 5]
print(podwoj_lista_skladana(liczby))
