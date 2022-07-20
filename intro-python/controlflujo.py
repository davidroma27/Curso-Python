# --- CONTROL DE FLUJO ---

# Doble igual: a == b
# a < b
# a > b
# a != b
# a <= b
# a >= b
#
# if 2 < 5:
#     print('2 es menor que 5')
#
# if 2 == 2:
#     print('2 es igual a 2')
#
# if 2 == 3:
#     print('2 es igual a 3')
#
# if 2 > 5:
#     print('2 es mayor a 5')
#
# if 5 > 2:
#     print('5 es mayor a 2')
#
# if 2 != 2:
#     print('2 es distinto a 2')
#
# if 3 != 2:
#     print('3 es distinto a 2')
#
# if 3 >= 2:
#     print('3 es mayor o igual a 2')
#
# if 3 <= 3:
#     print('3 es menor o igual a 3')


# --- if / elif / else ---
if 2 > 5:
    print('hola')
elif 2 < 5:
    print('2 menor a 5 en elif') # se imprime elif

# Si dos condiciones de un if se evaluan a TRUE se ejecutará siempre LA PRIMERA
if 2 < 5:
    print('2 menor a 5 en if')
elif 2 < 5:
    print('2 menor a 5 en elif')

# La condicion ELSE se ejecuta si todas las condiciones anteriores evaluan a FALSE
if 2 > 5:
    print('2 menor a 5 en if')
elif 2 > 5:
    print('2 menor a 5 en elif')
else:
    print('else: todo lo anterior es falso')

# if de una linea
if 2 < 5: print('if de una linea')

# Operador ternario
print('cuando devuelve true') if 2 < 5 else print('cuando devuelve false')

# --- AND y OR ---
# AND: El codigo se ejecuta SOLO si TODAS las condiciones son TRUE
# OR: El codigo se ejecuta si AL MENOS UNA condicion es TRUE
if 2 < 5 and 3 > 2:
    print('AND: ambas devuelven true')

if 2 > 5 and 3 > 2:
    print('AND: false porque no se cumplen ambas condiciones')

if 1 < 0 or 1 > 0:
    print('OR: una de las condiciones devuelve true')
if 1 < 0 or 0 > 1:
    print('OR: false porque ambas devuelven false')