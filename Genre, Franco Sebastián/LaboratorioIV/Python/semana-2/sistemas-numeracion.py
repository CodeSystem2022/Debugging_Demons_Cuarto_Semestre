# Profundizando en los sistemas de numeración:

# Sistema decimal:
a = 10
print(f"a decimal: {a}")

# Sistema Binario:
a = 0b1010
print(f"a binario: {a}")

# Sistema octal:
a = 0o12
print(f"a octal: {a}")

# Sistema hexadecimal:
a = 0xA
print(f"a hexadecimal: {a}")


# Base Decimal:
a = int('23', 10)
print(f"a = base decimal: {a}")

# Base Binario:
a = int('10111', 2)
print(f"a = base binario: {a}")

# Base Octal:
a = int('27', 8)
print(f"a = base octal: {a}")

# Base Hexadecimal:
a = int('17', 16)
print(f"a = base hexadecimal: {a}")

# Base 5 (sus valores son de 0 a 4):
a = int('344', 5)
print(f"a = base 5: {a}")

#Notacion exponencial (valores positivos o negativos):
a = 3e5
print(f'a: {a: .2f}') #valor positivo 

a = 3e-5
print(f'a: {a: .5f}') #valor negativo 

# Cualquier calculo que incluye un float, todo cambia a float .

a = 4.0 + 5 #convesion a tipo float 
print(a)
print(type(a))
