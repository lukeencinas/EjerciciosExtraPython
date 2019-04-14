"""
cadena1 = input('Introduce la primera cadena: ')
cadena2 = input('Introduce la segunda cadena: ')
cadena3 = cadena1[0:int(len(cadena1)/2)] + cadena2 + cadena1[int(len(cadena1)/2):]
print(cadena3) 
"""

"""
string = input('Introduce una cadena: ')
for i in range(len(string)):
    if i%2 == 0:
        print(string[i], end = ',')
"""

"""
lista=[1,4,62,78,32,23,90,24,2,34]
n = int(input('Introduce un numero '))
for i in lista:
    if i > n:
        print(i, end = ' ')
"""

"""
for i in range(1500,2801,5):
    if i%7 == 0: 
        print(i)
"""

"""
palabra = input('Introduce una palabra con letras y numeros: ')
char = 0
num = 0
for i in palabra:
    if i.islower() or i.isupper():
        char += 1
    elif i.isnumeric():
        num += 1
print('El string: ',palabra,' tiene ', char, ' caracteres y ', num, ' numeros')         
"""


mes = {'Ene': 31, "Feb": 28, "Mar": 31, "Abr": 30 , "May" : 31, "Jun": 30, "Jul": 31, "Ago": 30 , "Sep": 31, "Oct": 31, "Nov" : 30, "Dec": 31}
palabra = input('Escribe las 3 primeras letras del mes: ')
if palabra in mes.keys():
    print(mes[palabra])