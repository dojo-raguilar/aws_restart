# Lista de entrada desordenada
lista_desordenada = [3, 2, 5, 1, 2, 4, 6, 1, 3, 5, 7]

# Eliminar elementos duplicados usando un conjunto (set)
#Esta línea de código utiliza un conjunto (set) para eliminar elementos duplicados de la lista lista_desordenada. 
#y luego volvemos a convertir el conjunto en una lista utilizando list().

lista_desordenada = list(set(lista_desordenada))
'''
#Metodo tradicional
pares = []
for num in lista_desordenada: 
    if num % 2 == 0:
        pares.append(num)
print(pares)

impares = []
for num in lista_desordenada:
    if num % 2 != 0:
        impares.append(num)
print(impares)
'''
# Separar números pares e impares (comprensión de listas)
pares = [num for num in lista_desordenada if num % 2 == 0]
impares = [num for num in lista_desordenada if num % 2 != 0]


# Ordenar números pares en orden ascendente
pares.sort()

# Ordenar números impares en orden descendente
impares.sort(reverse=True)

# Unir las listas ordenadas para obtener el resultado final
resultado = pares + impares

# Imprimir el resultado
print(resultado)