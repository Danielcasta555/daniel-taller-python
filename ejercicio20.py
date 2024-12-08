# Escribe un programa que solicite al usuario un número entero positivo y
#  luego imprima si ese número es un palíndromo o no utilizando un bucle while.

n = int(input("introduce un numero entero positivo"))

numero_str = str(n)
longitud = len(numero_str)
es_palindromo = True

i = 1
while i < longitud // 2:
    if numero_str[i] != numero_str[longitud - 1 - i]:
        es_palindromo = False
        break
    i += 1

    if es_palindromo:
        print(f"{n} es un numero palindromo")
    else:
        print(f"{n}no es numero palindromo")