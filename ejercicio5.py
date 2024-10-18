# ejercicio 5
"""
escribe un programa que convierta un valor dado en grados fahrenheit a grados celsius

entrada:
   grados fahrenheit: int
salida:
   grados celsius 
   """
gradosfare = input("ingresa los grados fahrenheit:")
gradosfare = int(gradosfare)
celsius = gradosfare - 32
celsius = celsius * 5/9
print(" la conversion de fahrenheit:",celsius)
