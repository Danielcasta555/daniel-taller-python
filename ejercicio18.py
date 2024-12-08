# Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima si ese número es un número perfecto utilizando un bucle while.


numero = int(input("Introduce un número entero positivo: "))


suma_divisores = 0
contador = 1


while contador < numero:
    if numero % contador == 0:
        suma_divisores += contador
    contador += 1


if suma_divisores == numero:
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
