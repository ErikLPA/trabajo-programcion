import math
#autores:ERik Pinto
#autores:CLaudio abarca
operacion = input('''
######################################                 
# Bienvenido Nuestra Calculadora     #
#autores:ERik Pinto                  #
#autores:CLaudio abarca              #
######################################
# # # # #Bienvenidos al himalaya #####
######################################                 
#  Introduce una opción:             #
# + para suma                        #
# - para resta                       #
# * para multiplicación              #
# / para división                    #
# r para calcular la raíz cuadrada   #
# p para potencia                    #
######################################
########>>Itroduce una opción<<####### 
#####Presiona Enter para continuar####                

''')

number_1 = float(input('Introduce tu primer número: '))

# Si la operación no es la raíz cuadrada, solicita el segundo número
if operacion != 'r':
    number_2 = float(input('Introduce tu segundo número: '))

if operacion == '+':
    print('{} + {} = '.format(number_1, number_2))
    print("####",number_1 + number_2,"####")

elif operacion == '-':
    print('{} - {} = '.format(number_1, number_2))
    print("####",number_1 - number_2,"####")

elif operacion == '*':
    print('{} * {} = '.format(number_1, number_2))
    print("####",number_1 * number_2,"####")

elif operacion == '/':
    print('{} / {} = '.format(number_1, number_2))
    print("####",number_1 / number_2,"####")

elif operacion == 'p':
    print('{} ** {} = '.format(number_1, number_2))
    print("####",number_1 ** number_2,"####")


elif operacion == 'r':
    # Calcular la raíz cuadrada del primer número
    print('La raíz cuadrada de {} es {:.2f}'.format(number_1, math.sqrt(number_1)))

else:
    print('Operación no válida. Introduce una opción válida.')
