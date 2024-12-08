# Escribe un programa que solicite al usuario un número entero positivo y
#  luego imprima la suma de los primeros n términos
#  de la serie armónica utilizando un bucle while.

n = int(input("introduce un numero entero positivo:"))

suma_amornica = 0.0
contador = 1

while contador <= n:
    suma_amornica += 1 / contador
    contador += 1

    print(f"la suma de los primeros {n} terminos de la serie armonica es: {suma_amornica}")