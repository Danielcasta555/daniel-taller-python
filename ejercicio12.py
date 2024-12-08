# Escribe un programa que solicite al usuario un número entero positivo y
# luego imprima la secuencia de Fibonacci 
# hasta ese número utilizando un bucle while.

numero = int(input("Introduce un numero entero positivo"))
 
a, b = 0, 1

while a <= numero:
    print(a)
    a, b = b, a + b