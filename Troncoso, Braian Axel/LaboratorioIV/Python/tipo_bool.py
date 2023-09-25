
# Bool contiene valores de True y False
# Los tipos númericos, es false para el 0 (solamente 0), true para los demas valores, pueden ser positivos o negativos.

valor = 0 # False
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 1 # True
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 0.1 # True
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 0.0 # False
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

# Tipo String -> False '' Representa una cadena vacia, -> True para los demas valores.

valor = '' # False
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 'Hola' # True
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

# Tipo colecciones -> False para colecciones vacias
# Tipo colecciones -> True para todas las demas
# Lista
valor = [] # False
resultado = bool(valor)
print(f'valor de una lista vacia: {valor}, Resultado: {resultado}')

valor = [2, 3, 4] # True
resultado = bool(valor)
print(f'valor de una lista con elementos: {valor}, Resultado: {resultado}')

# Tupla

valor = () # False
resultado = bool(valor)
print(f'valor con una tupla vacia: {valor}, Resultado: {resultado}')

valor = (5,) # True
resultado = bool(valor)
print(f'valor con una tupla con elementos: {valor}, Resultado: {resultado}')

# Diccionario
valor = {} # False
resultado = bool(valor)
print(f'valor con un diccionario vacio: {valor}, Resultado: {resultado}')

valor = {'Nombre': 'Juan', 'Apellido': 'Perez'} # True
resultado = bool(valor)
print(f'valor con un diccionario con elementos: {valor}, Resultado: {resultado}')

# Sentencias de control con bool

if (1,): # Se puede probar con todos los ejemplos dados en esta clase que estan en la parte superior
    print('Regresa verdadero')
else:
    print('Regresa falso')

# Ciclos

variable = 0
while variable: # False
    if '':
        print('Regresa verdadero ciclo')
    else:
        print('Regresa falso ciclo') # False
    print('Regresa verdadero entró al ciclo')
    break
else:
    print('Regresa falso')
