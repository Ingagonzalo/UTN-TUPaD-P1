#Actividad N1
#Crea un "Hola Mundo!"

print("Hola Mundo!")


#-----------------------------------------------------------------------------------------------
#Actividad N2
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


#-----------------------------------------------------------------------------------------------
#Actividad N3
#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
pais = input("Ingrese su pais: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}.")

#-----------------------------------------------------------------------------------------------
#Actividad N4
#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = float(input("Ingrese el radio de un circulo: "))

pi = 3.1415926

perimetro = 2 * pi * radio

area = pi * radio ** 2

print(f" El area del circulo es de: {area} y su perimetro es de: {perimetro} ")


#-----------------------------------------------------------------------------------------------
#Actividad N5
#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = float(input("Ingrese los segundos: "))

horas =  segundos / 3600 

print(f"Los segundos ingresados: {segundos}s , equivalen a {horas}h de horas.")


#-----------------------------------------------------------------------------------------------
#Actividad N6
#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

tabla = int(input("Ingrese su tabla: "))

for i in range (1,11):
    
    resultado = i*tabla
    print(f"{tabla} * {i} = {resultado}")
    
print("Fin")


#-----------------------------------------------------------------------------------------------
#Actividad N7
#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingrese su primer valor: "))
numero2 = int(input("Ingrese su segundo valor: "))

print(f"La suma de los valores es de: {numero1 + numero2}")
print(f"La resta de los valores es de: {numero1 - numero2}")
print(f"La multiplicación de los valores es de: {numero1 * numero2}")
print(f"La división de los valores es de: {numero1 / numero2}")


#-----------------------------------------------------------------------------------------------
#Actividad N8
#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura en metros: "))

IMC = peso / (altura**2)

print(f"Su IMC es de: {IMC}" )


#-----------------------------------------------------------------------------------------------
#Actividad N9
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))

fahrenheit = ((9/5) * celsius) + 32

print(f"Su valor en celsius: {celsius}°C equivalen a {fahrenheit}°F ")


#-----------------------------------------------------------------------------------------------
#Actividad N10
#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

numero1 = float(input("Ingresa su primer valor: "))
numero2 = float(input("Ingresa su segundo valor: "))
numero3 = float(input("Ingresa su tercer valor: "))

promedio = (numero1 + numero2 + numero3)/3

print(f"El valor promedio de los valores {numero1}, {numero2}, {numero3} es de {promedio}")