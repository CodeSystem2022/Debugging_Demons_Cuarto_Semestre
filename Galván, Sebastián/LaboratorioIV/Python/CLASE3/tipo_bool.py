# Bool contiene los valores de True y False
# Los tips numéricos, es falsse para el 0 (cero), true para los demas valores

valor = 0
resultado = bool(valor)
print(f'valor: {valor}. Resultado: {resultado}')

valor = 1
resultado = bool(valor)
print(f'valor: {valor}. Resultado: {resultado}')

valor = 0,0
resultado = bool(valor)
print(f'valor: {valor}. Resultado: {resultado}')

valor = -1
resultado = bool(valor)
print(f'valor: {valor}. Resultado: {resultado}')

valor = 0.0
resultado = bool(valor)
print(f'valor: {valor}. Resultado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'valor: {valor}. Resultado: {resultado}')

# Tipo String -> False '', True demás valores
valor = ''
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 'hola'
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

# Tipo colecciones -> False para coleccioes vacias
# Tipo colecciones -> True para todas las demás

valor = []
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = [1, 2, 3]
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Tupla
valor = ()
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = (1,)
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Diccionario
valor = {}
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = {'a': 1}
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

# Senetencias de control con bool:

if '':
    print("Regresa verdadero")
else:
    print("Regresa Falso")

if bool(''):
    print("Regresa verdadero")
else:
    print("Regresa Falso")

if 0:
    print("Regresa verdadero")
else:
    print("Regresa Falso")

# Ciclos

variable = 0
while variable:
    print('Dentro del ciclo')
    break
else:
    print('No entre al ciclo')


