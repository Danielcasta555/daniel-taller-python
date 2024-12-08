# Escribe un programa que calcule la suma de los números pares 
# del 1 al 100 utilizando un bucle while.

suma_pares = 0
numero = 2

while numero <=100:
    suma_pares += numero
    numero += 2
    print(f"La suma de los pares del 1 al 100 es: {suma_pares}")