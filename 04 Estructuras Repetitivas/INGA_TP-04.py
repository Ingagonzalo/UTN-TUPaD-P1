"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

cantNum = 100

for i in range(cantNum+1):
    print(i)
    
#---------------------------------------------------------------------------------------------

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

numero = abs(int(input("Ingrese el numero entero: "))) #recibo un entero y lo paso a positivo
contador = 0

while numero > 0:
    numero = numero // 10
    contador += 1

print(f"El número ingresado tiene {contador} dígito(s).")

#---------------------------------------------------------------------------------------------

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

valorMax= int(input("Ingrese su numero maximo: "))
valorMin= int(input("Ingrese su numero minimo: "))

#version con For

for numero in range(valorMin+1, valorMax):
    print(numero)
    numero += 1
    
#version con While

"""valorMin += 1

while valorMin < valorMax :
    print(valorMin)
    valorMin += 1"""
    
#---------------------------------------------------------------------------------------------

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

numeroIngresado = 1 
acumulador = 0

while numeroIngresado != 0:
    numeroIngresado = int(input("Ingrese un numero entero: "))
    acumulador = numeroIngresado + acumulador

print(f"El total acumulado es de: {acumulador}")
    
#---------------------------------------------------------------------------------------------

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random

numeroAleatorio = random.randint(0, 9)
numeroIngresado = 10
acumulador = 0

while numeroAleatorio != numeroIngresado:
    numeroIngresado = int(input("Ingrese su numero: "))
    acumulador += 1

print(f"El numero a adivinar era el {numeroAleatorio} y le tomo {acumulador} intentos adivinarlo.")

#---------------------------------------------------------------------------------------------

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""


numerosPares = 0

for i in range(100, -1, -2):
    print(i)
    
#---------------------------------------------------------------------------------------------

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

numeroMax = int(input("Ingrese el numero maximo para calcular: "))
acumulador = 0

for numero in range(numeroMax+1):
    acumulador = numero + acumulador
    
print(f"El total calculado desde el 0 hasta el {numeroMax} es de {acumulador}")

#---------------------------------------------------------------------------------------------

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

cantNumero = 10 #modificable a 100
numeroEntero = 0
acumNegativo = 0
acumPositivo = 0
acumPar = 0
acumImpar = 0

for contador in range(10):
    numeroEntero = int(input("Ingrese su numero entero: "))
    if numeroEntero < 0:
        numeroEntero = abs(numeroEntero)
        acumNegativo += 1
    else:
        acumPositivo += 1
    
    if numeroEntero % 2 == 0 :
        acumPar += 1
    else:
        acumImpar +=1

print(f"En el rango de los {cantNumero} numeros, se encuentran: \n {acumNegativo}: Numeros Negativos \n {acumPositivo}: Numeros Positivos \n {acumPar}: Numeros Pares \n {acumImpar}: Numeros Impares")

#---------------------------------------------------------------------------------------------

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

cantNumeros = 10
numero = 0
contador = 1
acumulado = 0
media = 0

while contador < cantNumeros + 1:
    numero = int(input(f"Ingrese el numero {contador}: "))
    contador += 1
    acumulado = acumulado + numero

media = acumulado / cantNumeros
print(f"La media de los {cantNumeros} numeros ingresados es de: {media}")

#---------------------------------------------------------------------------------------------

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

numero = int(input("Ingrese un número entero: "))
numOriginal = numero  # Guardamos una copia del número original
numInvertido = 0

while numero > 0:
    digito = numero % 10      # Obtenemos el último dígito
    numInvertido = numInvertido * 10 + digito  # Lo agregamos al número invertido
    numero = numero // 10     # Eliminamos el último dígito

print(f"El número {numOriginal} invertido es: {numInvertido}")