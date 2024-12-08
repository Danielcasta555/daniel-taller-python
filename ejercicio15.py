# Escribe un programa que imprima los números primos del 1 al 100 
# utilizando un bucle while.

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
         return False 
    return True

contador = 1

while contador <= 100:
    if es_primo(contador):
        print(contador)
    contador += 1
