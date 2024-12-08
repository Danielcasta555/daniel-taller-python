# Escribe un programa que solicite al usuario un número entero positivo y
#luego imprima los números del 1 hasta ese número utilizando un bucle while.

n = int(input("Introduce un numero entero positivo: "))

contador = 1

while contador <= n:
    print(contador)
    contador +=1