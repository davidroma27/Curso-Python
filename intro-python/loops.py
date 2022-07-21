# --- WHILE ---
i = 0

# while i < 5:
#     print(i)
#     i += 1

# Uso de break y continue
# Break hace que al cumplirse la condicion salga del loop
# while i < 5:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# Continue hace que se vuelva a la linea del while para comprobar la condicion
# while i < 5:
#     i += 1
#     if i == 3:
#         continue # Cuando i == 3 vuelve a while y no se imprime
#     print(i)

# --- FOR ---
# Se usa para iterar sobre listas, tuplas, diccionarios...
usuarios = ['bbito', 'fiufiu', 'mac', 'cheese']

# for user in usuarios:
#     print(user)

# Itera sobre los caracteres de un String
usuario = 'macncheese'


# for c in usuario:
#     print(c)

# Recorre la lista hasta que encuentra el elemento que cumple la condicion y lo imprime
# for user in usuarios:
#     if user == 'mac':
#         break
#     print(user)

# Igual que en while tambien se puede usar CONTINUE
# for user in usuarios:
#     if user == 'mac':
#         continue # nos saltamos el elemento de la condicion y imprime el resto
#     print(user)


# Uso de RANGE
# for x in range(0,6):
#     print(x) # OJO: No imprime el 6 porque el rango es 0,1,2,3,4,5

# Los RANGE tambien se pueden incrementar por un numero dado
# for x in range(3, 30, 5):
#     print(x) # Imprime elementos de 5 en 5 que esten dentro del rango
# else: # En for loop tambien se puede usar ELSE (Funciona como "default")
#     print('Hemos terminado')

# Bucles FOR anidados
# edades = [23, 25, 26, 52]
#
# # IMPORTANTE: Para cada usuario itera sobre TODAS las edades antes de pasar al siguiente usuario
# for user in usuarios:
#     for edad in edades:
#         print(user, edad)



