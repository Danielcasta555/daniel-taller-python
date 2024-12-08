# Escribe un programa que calcule el factorial de un número ingresado por el usuario 
# utilizando un bucle while.

numero = int(input("Ingrese un numero para calcular su factorial: "))

factorial = 1

while numero > 1:
     factorial *= numero
     numero -= 1
     print(f"el factorial es: {factorial}")




