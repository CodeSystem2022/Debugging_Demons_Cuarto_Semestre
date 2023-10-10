# Profundizando en el tipo float

a = 3.0
# Constructor de tipo float -> puede recibir enteros y de tipo string

a = float(10) # Le pasamos directamente un tipo entero (int)
a = float('10')
print(f'a: {a:.2f}')

# Notación exponencial (Valores positivos o negativos)
a = 3e5
print(f'a: {a:.2f}')

a = 3e-5
print(f'a: {a:.2f}')

# Cualquier calculo que cambie incluya un float, todo cambia a float
a = 4.0 + 5
print(a)
print(type(a))
