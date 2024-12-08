# Escribe un programa que imprima los números del 1 al 100 que sean múltiplos de 
# 3 utilizando un bucle while.

contador = 1 

while contador <= 100:
    if contador % 3 == 0:
        print(contador)
    contador += 1