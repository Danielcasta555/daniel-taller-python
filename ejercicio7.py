# Escribe un programa que solicite al usuario un número entero positivo y luego imprima la suma de los dígitos de ese número utilizando 
# un bucle while.

numero = int(input("Intoduce un numero entero positivo:"))
suma_digitos = 0 

while numero > 0:
    digitos = numero % 10 
    suma_digitos += digitos
    numero = numero // 10
    print(f"La suma de los digitos es: {suma_digitos}")


