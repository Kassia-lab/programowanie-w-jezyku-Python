def przetworz_listy(lista1, lista2):
    polaczona = lista1 + lista2
    bez_duplikatow = list(set(polaczona))
    wynik = [x ** 3 for x in bez_duplikatow]
    return wynik


wynik = przetworz_listy([1, 2, 3], [2, 3, 4])


print(wynik)
