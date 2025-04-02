#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingresa su edad: "))

if edad >= 18:
    print(f"Su edad es de {edad} y es mayor de edad")
else:
    print(f"Su edad es de {edad} y es menor de edad")

#---------------------------------------------------------------------------------------------------------------------

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print(f"Su nota es de {nota} y usted esta Aprobado")
else: 
    print(f"Su nota es de {nota} y usted esta Desaprobado")

#---------------------------------------------------------------------------------------------------------------------

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un numero par: "))

if (numero % 2) == 0:
    print(f"Ha ingresado un número par")
else:
    print(f"Por favor, ingrese un número par")

#---------------------------------------------------------------------------------------------------------------------
    
"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
"""
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Usted es un niño.")
elif edad >= 12 and edad < 18:
    print("Usted es un adolescente.")
elif edad >= 18 and edad < 30:
    print("Usted es un Adulto/a joven.")
else:
    print("Usted es un Adulto/a ")

#---------------------------------------------------------------------------------------------------------------------
    
"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
"""

contrasenia = input("Ingrese su contraseña: ")

if len(contrasenia) >= 8 and len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta")

else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#---------------------------------------------------------------------------------------------------------------------

"""Escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
"""

import random
from statistics import mode, median, mean


numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcular la media, mediana y moda
media_promedio = mean(numeros_aleatorios)
valor_medio = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)


if media_promedio > valor_medio > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media_promedio < valor_medio < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo"

print(f"Lista de números: {numeros_aleatorios}")
print(f"Media: {media_promedio}")
print(f"Mediana: {valor_medio}")
print(f"Moda: {moda}")
print(f"Resultado: {sesgo}")

#---------------------------------------------------------------------------------------------------------------------

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla."""

palabraFrase = input("Ingrese su palabra o frase: ")

ultimaLetra = palabraFrase[-1].lower() # Obtengo la ultima letra de la frase y lo paso a minuscula

if ultimaLetra == "a" or ultimaLetra == "e" or ultimaLetra == "i" or ultimaLetra == "o" or ultimaLetra == "u":
    palabraFrase = palabraFrase + "!"  
else:
    palabraFrase = palabraFrase
    

print(palabraFrase)

#---------------------------------------------------------------------------------------------------------------------

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""

nombre = input("Ingrese su nombre: ")
print("Seleccione la opcion que desee: \n 1. Si quiere su nombre en mayúsculas. \n 2. Si quiere su nombre en minúsculas.\n 3. Si quiere su nombre con la primera letra mayúscula. ")
opcion = int(input("Seleccione la opcion: "))

if opcion == 1:
    nombre = nombre.upper()
elif opcion == 2:
    nombre = nombre.lower()
else:
    nombre = nombre.title()

print(nombre)

#---------------------------------------------------------------------------------------------------------------------

"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""

magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >=3 and magnitud < 4:
    print("Leve, ligeramente perceptible")
elif magnitud >=4 and magnitud < 5:
    print("Moderado, sentido por personas, pero generalmente no causa daños")
elif magnitud >=5 and magnitud < 6:
    print("Fuerte, puede causar daños en estructuras débiles")
elif magnitud >=6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")
    

#---------------------------------------------------------------------------------------------------------------------

"""10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ").upper() #Minimizamos errores al ponerlo como mayuscula
mes = int(input("Ingrese el numero del mes en el que se encuentra: "))
dia = int(input("Ingrese el numero del dia en el que se encuentra: "))

if hemisferio == "N" and (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12): #Verificamos que los dias y el mes este dentro de los valores correctos
    if (mes == 12 and dia > 21) or (mes <= 3 and dia <= 20): 
        print("Usted se encuentra en Invierno")
    elif (mes >= 3 and dia >= 21) and (mes <= 6 and dia <= 20):
        print("Usted se encuentra en Primavera")
    elif (mes >= 6 and dia >= 21) and (mes <= 9 and dia <= 20):
        print("Usted se encuentra en Verano")
    elif (mes >= 9 and dia >= 21) and (mes <= 12 and dia <= 20):
        print("Usted se encuentra en Otoño")
    else:
        print("Usted no ingreso correctamente sus datos")
elif hemisferio == "S" and (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12): #Verificamos que los dias y el mes este dentro de los valores correctos
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20): 
        print("Usted se encuentra en Verano")
    elif (mes >= 3 and dia >= 21) and (mes <= 6 and dia <= 20):
        print("Usted se encuentra en Otoño")
    elif (mes >= 6 and dia >= 21) and (mes <= 9 and dia <= 20):
        print("Usted se encuentra en Invierno")
    elif (mes >= 9 and dia >= 21) and (mes <= 12 and dia <= 20):
        print("Usted se encuentra en Primavera")
    else:
        print("Usted no ingreso correctamente sus datos")
else:
    print("Usted no ingreso correctamente sus datos")