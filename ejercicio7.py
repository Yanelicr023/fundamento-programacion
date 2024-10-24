'''
realizar un programa  que reciba una cantidad de minutos y muestre por pantall a cuantas horas y minutos corresponde
Entrada:
   minutos : int
Salida:
   minutos y horas correspondientes 
'''
minutos = input("ingresa los minutos: ") 
minutos = int (minutos)
horas = minutos/60
minutores = minutos%60
print("las horas son : ", horas ,minutos)
