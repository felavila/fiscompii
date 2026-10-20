# ==========================================
# Comentarios
# ==========================================

# Esto es un comentario de una línea

"""
Esto puede usarse como
un comentario de varias líneas
"""


# ==========================================
# Operaciones básicas
# ==========================================

# Suma
1 + 1

# Resta
5 - 2

# Multiplicación
3 * 4

# División
10 / 2

# División entera
10 // 3

# Resto de una división
10 % 3

# Potencia
2 ** 3

# Raíz cuadrada
4 ** 0.5

# Otra forma de calcular raíces cuadradas
import math

math.sqrt(4)
math.sqrt(16)

#Si quiero saber más sobre math
help(math)

# ==========================================
# Variables
# ==========================================

x = 2
y = 2.0

print(x)
print(y)

# Ver el tipo de variable
print(type(x), type(y))

# int   -> número entero
# float -> número decimal

nombre = "Python"
activo = True

print(type(nombre))
print(type(activo))


# ==========================================
# Operaciones con variables
# ==========================================

x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)


# ==========================================
# Comparaciones
# ==========================================

x = 5

print(x == 5)   # igual
print(x != 5)   # diferente
print(x > 3)    # mayor que
print(x < 10)   # menor que
print(x >= 5)   # mayor o igual
print(x <= 5)   # menor o igual


# ==========================================
# Listas
# ==========================================

numeros = [1, 2, 3, 4, 5]

print(numeros)

# Primer elemento
print(numeros[0])

# Último elemento
print(numeros[-1])

# Largo de la lista
print(len(numeros))


# ==========================================
# Tuplas
# ==========================================

tupla = (1, 2, 3)

# ==========================================
# Loops
# ==========================================

# Loop sobre una lista

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)


# Loop usando range

for i in range(5):
    print(i)

# Resultado:
# 0
# 1
# 2
# 3
# 4


# Elegir inicio y final

for i in range(1, 6):
    print(i)


# Elegir el paso

for i in range(0, 10, 2):
    print(i)

# Resultado:
# 0
# 2
# 4
# 6
# 8


# ==========================================
# Operaciones dentro de un loop
# ==========================================

for i in range(1, 6):

    cuadrado = i ** 2
    raiz = i ** 0.5

    print(i, cuadrado, raiz)


# ==========================================
# While loop
# ==========================================

x = 0

while x < 5:
    print(x)
    x = x + 1


# ==========================================
# Condiciones
# ==========================================

x = 10

if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual a 5")


# ==========================================
# Condiciones dentro de loops
# ==========================================

for i in range(10):

    if i % 2 == 0:
        print(i, "es par")
    else:
        print(i, "es impar")
# ==========================================
# Diccionarios
# ==========================================

# Los diccionarios guardan información usando
# pares de clave : valor

persona = {
    "nombre": "Felipe",
    "edad": 33,
    "ciudad": "Santiago"
}

print(persona)

# Acceder a un valor usando su clave
print(persona["nombre"])
print(persona["edad"])

# Agregar un nuevo elemento
persona["profesion"] = "Astronomo"

print(persona)

# Modificar un valor
persona["edad"] = 34

# Eliminar un elemento
del persona["ciudad"]

print(persona)


# Ver todas las claves
print(persona.keys())

# Ver todos los valores
print(persona.values())

# Ver claves y valores
print(persona.items())