
# Bool contiene ,os valores de True y False
# Loa tipos numericos, es false para el 0 (cero). true para los demas valores
valor = 0
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 22
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')


# Tipo String -> False '', True para los demas valores
valor = ''
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

# Tipo de colecciones -> False para colecciones vacias
# -> True para todas las demas
# Lista
valor = []
resultado = bool(valor)
print(f'valor de una tupla vacia: {valor}, Resultado: {resultado}')

valor = [2,3,4]
resultado = bool(valor)
print(f'valor de una tupla de elementos: {valor}, Resultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
print(f'valor de una lista vacia: {valor}, Resultado: {resultado}')

valor = (1,3,4)
resultado = bool(valor)
print(f'valor de una lista con elementos: {valor}, Resultado: {resultado}')

# Diccionario
valor = {}
resultado = bool(valor)
print(f'valor de un diccionario vacio: {valor}, Resultado: {resultado}')

valor = {'Nombre ': 'Juan', 'Apellido ': 'Perez'}
resultado = bool(valor)
print(f'valor de un diccionario con elementos: {valor}, Resultado: {resultado}')

# Sentencias de control con bool
if '':
    print('el if regresa verdadero')
else:
    print('el if Regresa falso')

if valor:
    print('el if Regresa verdadero')
else:
    print('el if Regresa falso')

# Ciclos
variable = 3
while variable:
    print('El ciclo regresa verdadero')
    break
else:
    print('El ciclo regresa falso')