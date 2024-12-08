# Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima los números impares desde 1 
# hasta ese número utilizando un bucle while.

numero = int(input("Introduce un numero entero positivo:"))

contador = 1

while contador <= numero:
    if contador % 2 !=0:
        print(contador)
        contador +=1