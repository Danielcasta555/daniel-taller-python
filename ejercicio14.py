# Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima los divisores de ese número utilizando un bucle while.

numero = int(input("Introduce un numero entero positivo"))

if numero > 0:
    divisor = 1
    print(f"los divisores de {numero} son:")

    while divisor <= numero:
        if numero % divisor == 0:
            print(divisor)
        divisor += 1
else:
    print("Introduce un numero positivo.")