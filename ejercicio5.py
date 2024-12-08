# Escribe un programa que solicite al usuario un número entero y luego 
# imprima los números pares desde 2 hasta ese número utilizando un bucle while.

n = int(input(f"Introduce un numero entero:"))
contador = 2

while contador <n:
    print(contador)
    contador += 2