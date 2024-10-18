#cera un programa que calcule area y perimetro de un rectangulo 
#entradas:
#base:integer
#altura:integer

#salida
#area:integer
#perimetro:integer

base = input("ingrsa la base:")
base = int(base)
altura = input("ingresa la altura:")
altura = int(altura)
area = base * altura
perimetro = (base + altura) * 2
print("el area del rectangulo es ", area)
print("el perimetro del rectangulo es", perimetro)
