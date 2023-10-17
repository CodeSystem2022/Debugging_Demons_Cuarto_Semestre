import math
from decimal import Decimal

# NaN (Not a number)
a = float('NaN') # Esto no va a dar salida de NaN.
print(f'{a}')

# Modulo math - Constructor float
a = float('Nan') # Python no es sensible con las mayusculas y minusculas.
print(f'Es de tipo NaN(Not a number)?: {math.isnan(a)}')
# Modulo decimal - Constructor Decimal
a = Decimal('nan') # Python no es sensible con las mayusculas y minusculas.
print(f'Es de tipo NaN(Not a number)?: {math.isnan(a)}')
