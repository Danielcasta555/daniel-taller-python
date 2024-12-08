# Escribe un programa que calcule la suma de los primeros 100 
# números naturales utilizando un bucle while.

n = 100
suma = 0
contador = 1 

while contador <= n:
    suma += contador 
    contador += 1
    print(f"La suma de los primerso {n} numeros naturales es: {suma}")