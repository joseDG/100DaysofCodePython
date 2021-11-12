"""num_char = len(input("What your name? "))
new_num_char = str(num_char)
print("Your name contains " + new_num_char + "chacters")

a = float(123)
print(type(a))

print(70 + float("100.5"))
"""

# Ejercicio3
# Escribe un programa que agregue 2 digitos ejm. si la entrada es
# 35 , entoences la salida tieen que ser 3 + 5 = 8
"""
two_digit_num = input("Ingresa un digito de 2 numeros: ")

first_digit = two_digit_num[0]
second_digit = two_digit_num[1]

result = int(first_digit) + int(second_digit)
print(result)
"""


# Ejercicio2
""""
height = float(input("Ingrese tu altura in m: "))
weight = float(input("Ingrese tu peso en kg: "))

BMI = weight / height**2

print(BMI)
"""

# Ejercicio3
""""
age = input("Cual es tu edad actual?")

age = 90 - int(age)
days = int(age)*365
weeks = int(age)*52
months = int(age)*12
print(f"Tu tienes {days} dias, {weeks} semanas y {months} meses restantes.")
"""
# Ejercicio4
print("Bienvenido ala calculadora de  propinas")
total = float(input("Cual fue la factura total? $"))
propina = int(input("Cuanta propina te gustaria dar? 10,12, or 15?"))
persona = int(input("Cuantas personas para dividir la cuenta?"))
calcular_propina = propina / 100 * total + total
separar_total = calcular_propina / persona
redondeo = round(separar_total, 2)

mensaje = f"Cada persona debe pagar:${redondeo}"
print(mensaje)
