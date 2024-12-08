# Escribe un programa que solicite al usuario un número entero positivo y
#  luego imprima la tabla de multiplicar de ese número utilizando un bucle while.

numero = int(input("introduce un numero positivo:"))

contador = 1 

while contador <= 10:
    print(f"{numero} X {contador} = {numero * contador}")
    contador = 1