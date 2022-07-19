if 3 > 5:
    print("5 es mayor a 3")  # Este codigo es inalcanzable porque siempre se ejecutara la condicion que evalua TRUE

# EN PYTHON LA ARQUITECTURA DEL CODIGO DEPENDE DE LA >>>IDENTACION<<< en lugar de llaves o corchetes

# if 5 > 3:
# print("5 es mayor a 3")

x = 5
y = 'bebito fiu fiu'

email = 'bbitofiufiu@gmail.com'

# print(x,y) #Pasamos parametros a la funcion print para mostrarlos en pantalla
# print(email)

# FORMAS DE DECLARAR VARIABLES:
mi_var = 'bbitofiufiu'
_mi_var = 'bbitofiufiu'
miVar = 'bbitofiufiu'
MIVAR1 = 'bbitofiufiu'  # No se podrán usar numeros al COMIENZO de una variable

a, b, c = 'mi', 'bbito', 'fiufiu'  # se puede asignar valores a varias variables en una misma linea
# print(a,b,c)

valor1 = valor2 = valor3 = 'bbitofiufiu'  # Se puede asignar un mismo valor a multiples variables a la vez
# print(valor1,valor2,valor3)

inicio = 'hola '
final = 'mundo'

# print(inicio + final) #concatenación de variables mediante +
# print(inicio, final) #concatenacion mediante coma. La coma introduce un espacio adicional

# --- TIPOS DE DATOS ---

# --- Strings ---
palabra = 'hola mundo'
frase = "hola mundo comilla doble"

# --- Numeros ---
entero = 20  # integer
decimales = 20.2  # float
complejo = 1j  # numero complejo

# print(palabra, frase, entero, decimales, complejo)


# --- Listas [] ---

listaVacia = []  # crea una lista vacía
lista = [1, 2, 3]  # crea lista con 3 elementos
lista2 = lista.copy()  # copia el contenido de una lista en otra lista
lista.append(4)  # append añade un elemento a una lista existente
# lista.clear() #borra el contenido de una lista

# print(lista, lista2)
# print(lista.count(4), lista2.count(4)) #count() devuelve el numero de ocurrencias de un elemento en una lista
# print(len(lista), len(lista2)) #len() devuelve el numero de elementos que contiene una lista

# Otra forma de hacerlo (mas codigo pero mas intuitivo)
largoLista = len(lista)
largoLista2 = len(lista2)

# print(largoLista, largoLista2)

listaPalabras = ['hola', 'mundo', 'bbitofiufiu']
# print(listaPalabras[0]) #imprime el PRIMER ELEMENTO de una lista

# borrado de elementos de una lista
# print(listaPalabras)
# listaPalabras.pop() #elimina el ultimo elemento de una lista
# print(listaPalabras)
# listaPalabras.remove('hola') #Elimina un elemento por su valor
# print(listaPalabras)

listaPalabras.reverse()  # invierte los elementos de la lista
# print(listaPalabras)
listaPalabras.sort()  # ordena los elementos de una lista. TODOS LOS ELEMENTOS DEBEN SER DEL MISMO TIPO DE DATO
# print(listaPalabras)  # en este caso ordena los string en orden alfabetico

# --- Tuplas () ---
# LAS TUPLAS NO SE PUEDEN MODIFICAR UNA VEZ CREADAS
# PARA MODIFICARLA HABRA QUE CREAR UNA COPIA Y TRANSFORMARLA EN LISTA
tupla = ('hola', 'mundo', 'bbitofiufiu', 'tupla')  # una TUPLA se declara con parentesis
# print(tupla.index('mundo'))  # devuelve la posicion de un elemento en la tupla
# print(tupla[0])  # devuelve el primer elemento

# las tuplas NO SON MODIFICABLES. Para ello tenemos que transformarla en una lista
listaDeTupla = list(tupla)
listaDeTupla.append('caramelo')
# print(listaDeTupla)

# --- Rangos ---
rango = range(6)
# print(rango)

# --- Diccionarios ---
# Son una coleccion de propiedades y valores
diccionario = {
    "nombre": "Kylo",
    "raza": "Persa",
    "edad": 1
}

# print(diccionario)  # imprime todas las propiedades y valores
# print(diccionario['nombre'])  # imprime el valor de una propiedad
# print(diccionario.get('nombre'))  # puedo acceder al valor con el metodo get()
diccionario['nombre'] = 'Fluffy'  # Para cambiar el valor de una propiedad
# print(len(diccionario))  # imprime el numero de elementos del diccionario

diccionario['ronronea'] = 'Si'  # añade una propiedad y valor nuevos
# print(diccionario)

# diccionario.pop('ronronea')  # elimina una propiedad
# diccionario.popitem()  # elimina la ULTIMA propiedad insertada
# del diccionario['ronronea']  # otra forma de eliminar una propiedad
# print(diccionario)

# copiaDic = diccionario.copy()  # copia el contenido de un diccionario en otro
copiaDic = dict(diccionario)
diccionario.popitem()
# print(diccionario, copiaDic)
diccionario.clear()  # elimina todas las propiedades del diccionario

# Diccionarios anidados
# gatitos = {
#
#     "Fluffy": {
#         "nombre": "Fluffy",
#         "edad": 4
#     },
#     "Neeko": {
#         "nombre": "Neeko",
#         "edad": 3
#     }
# }

# Otra forma de declarar diccionarios anidados
fluffy = {
    "nombre": "Fluffy",
    "edad": 4
}
neeko = {
    "nombre": "Neeko",
    "edad": 3
}
gatitos = {
    "Fluffy": fluffy,
    "Neeko": neeko
}

print(gatitos)

# Crear diccionarios mediante DICT
perros = dict(nombre="bbito fiufiu", edad=5)
print(perros)

# --- Booleanos ---
verdadero = True
falso = False

print(verdadero, falso)
