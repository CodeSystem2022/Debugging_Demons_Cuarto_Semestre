# Profundizando en el tipo float
a = 3.0
print(f'a: {a:.2f}')

# Constructor de tipo float -> puede recibir enteros y de tipo String
a = float(10) # Le pasamos un tipo entero (int)
print(f'a: {a:.2f}')
a = float('10')
print(f'a: {a:.3f}')

# Notacion exponencial (valores positivos o negativos)
a = 3e5
print(f'a: {a:.2f}')

a = 3e-5
print(f'a: {a:.5f}')

# Cualquier calculo que incluye un float, todo cambia a float
a = 4.0 + 5
print(a)
print(type(a))

# Toda variable o literal que se utilice en una expresion donde se involucra un tipo float
# el resultado final de esta, es una conversion de tipo float



