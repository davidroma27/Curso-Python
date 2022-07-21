# --- FUNCIONES ---
# Las funciones se declaran mediante "def"
def myFunc():
    print('Mi primera funcion')


# Llamamos a la funcion
# myFunc()

# for i in range(0,6):
#     myFunc() #Imprime la funcion 6 veces

# def imprimeDato(arg1):  # Declaramos una funcion con 1 argumento
#     print('Mi argumento es', arg1)
#
#
# imprimeDato('parametro 1')  # Llamamos a la funcion y le pasamos 1 parametro
#
#
# def imprimeNombre(nombre, apellido):
#     print('El nombre completo es: ', nombre, apellido)


# Si le pasamos menos de 2 parametros se producirá una excepcion
# imprimeNombre('bbito', 'fiufiu')


# funciones con ARGUMENTOS VARIABLES
# def imprimeDato2(*nombre):  # Con * se indica que el numero de argumentos que puede tomar es variable
#     print('El nombre completo es: ', nombre)
#     print('El solo nombre: ', nombre[1]) # Se puede imprimir un solo elemento


# IMPORTANTE: Los argumentos que pasamos se crearan como una TUPLA
# imprimeDato2('mac', 'cheese', 'bbito', 'fiufiu')

# def nombreCompleto(apellido, nombre):
#     print(nombre, apellido)

# Se pueden asignar valores a los parametros en distinto orden de los argumentos
# nombreCompleto(nombre='Mac', apellido='Cheese')

# **kwargs permite acceder a los argumentos utilizando la sintaxis de DICCIONARIO
# def nombreCompleto2(**kwargs):
#     print(kwargs['nombre'], kwargs['apellido'])
#
# nombreCompleto2(nombre='Mac', apellido='Cheese')


# --- MAS FUNCIONES ---
# A una funcion se le puede pasar un valor por defecto de un argumento aunque despues sea distinto al llamar a la funcion
# def myFunc2(arg = 'bbito'):
#     print(arg)
#
# # Si al llamar a la funcion no se pasa ningun parametro devolvera el valor por defecto
# myFunc2()
# myFunc2('fiufiu')

# def miFuncionLista(lista):
#     for e in lista:
#         print(e)
#
# miFuncionLista(['bbito', 'fiufiu']) # Imprime los elementos que se pasan por parametro como una lista

# def concatNombres(lista):
#     i = ''
#     for e in lista:
#         i = i + e + ' '
#     return i
#
# # Para devolver los nombres de la lista concatenados es necesario almacenar la salida de la funcion en una variable
# nombres = concatNombres(['bbito', 'fiufiu'])
# print(nombres)

# --- RECURSIVIDAD ---
# Funcion recursiva que devuelve los elementos en orden decreciente
def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)

# Las funciones recursivas son utiles para:
#   -Iterar sobre colecciones de datos
#   -Realizar intentos a la conexion de APIs o BD
#   -Procesamiento por lotes (batch)
