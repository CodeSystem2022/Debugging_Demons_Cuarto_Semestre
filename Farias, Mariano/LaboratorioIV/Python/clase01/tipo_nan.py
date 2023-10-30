import math
from decimal import Decimal

# NaN (Not a Number)
a = float('Nan')
print(f'a: {a}')

# Módulo math
a = float('nan')
print(f'Es de tipo NaN(Not a Number)?: {math.isnan(a)}')

# Módulo decimal
a = Decimal('NaN')
print(f'Es de  tipo NaN(Not a Number)?: {math.isnan(a)}')