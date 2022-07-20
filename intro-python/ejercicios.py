# --- Ejercicio 1 ---
# dato = input('Introduce dato: ')
#
# lista = ['hola', 'mundo', 'bbito', 'fiufiu']
#
# if lista.count(dato) > 0:
#     print('El dato existe:', dato)
# else:
#     print('El dato no existe:', dato)

# --- Ejercicio 2 ---
# Pequeña calculadora que pide dos valores por teclado y se valida cada uno despues de ser introducido
# uso de TRY / EXCEPT para la gestion de excepciones si se introduce un dato no valido
n1 = input('Introduce primer numero: ')

try:
    n1 = int(n1)
except:
    n1 = 'exception'  # Si el dato no se convierte a int se produce una excepcion

if n1 == 'exception':
    print('El numero introducido no es correcto')
    exit()

n2 = input('Introduce segundo numero: ')

try:
    n2 = int(n2)
except:
    n2 = 'exception'

if n2 == 'exception':
    print('El numero introducido no es correcto')
    exit()

operador = input('Introduce operación: ')

if operador == '+':
    print('Suma:', n1 + n2)
elif operador == '-':
    print('Resta', n1 - n2)
elif operador == '*':
    print('Multiplicacion', n1 * n2)
elif operador == '/':
    print('Division', n1 / n2)
else:
    print('El operador introducido no es valido')

# print(n1 + n2)  # PARA REALIZAR UNA SUMA DENTRO DE UN PRINT HAY QUE ASEGURARSE QUE LOS DATOS SEAN INT
