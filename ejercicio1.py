#suma de los primeros n números naturales: 
# Calcula la suma de los números desde 1 hasta n 
# utilizando un ciclo for. Itera sobre los números en el rango de 
# 1 a n y acumula su suma.

#definir la funcion para calcular la suma de los primeros n numeros naturales 
def suma_numeros_naturales(n):
    suma = 0
#itera sobre rango 1 a n (incluyendo n)
    for numero in range (1, n + 1):  # type: ignore
        suma += numero
    return suma

# ejemplo de uso de la funcion 
n = 10 
resultado = suma_numeros_naturales(n)
print(f"la suma de los primeros {n} numeros naturales es: {resultado}")

