#ejercicio 3
#programa que calcular la hipotenusa de un triangulo a partir de sus catetos
#entrada:
#cateto1:int
#cateto2:int

#salida:
#hipotenusa

#analisis:resuelve con el teorema de pitagoras

cateto1 = input("escribe el cateto1:")
cateto1 = int(cateto1)
cateto2 = int(input('escribe el cateto 2:'))
hipotenusa = cateto1 * cateto1 + cateto2 * cateto2
hipotenusa = hipotenusa ** (1/2)
print('la hipotenusa es:',hipotenusa)
