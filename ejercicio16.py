# Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima si ese número es primo o no utilizando un bucle while.

numero = int (input("Introduce un numero entero positivo:"))

if numero > 1:
    es_primo = True
    divisor = 2 

while divisor <= numero //2:
    if numero % divisor ==0:
        es_primo = False
        break 
    divisor += 1

    if es_primo:
        print(f"el numero {numero} es primo.")
    else: 
        print(f"el numero {numero} no es primo")
else:
    print("introduce un numero entero pisitivo mayo que 1")