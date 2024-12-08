# Escribe un programa que solicite al usuario un número entero y 
# luego imprima los primeros n términos de
#  la secuencia de Fibonacci utilizando un bucle while.

n = int(input("Introduce un numero entero pisitivo:"))

a, b = 0, 1
Contador = 0

while Contador < n:
    print(a)
    a, b = b, a + b
    Contador += 1