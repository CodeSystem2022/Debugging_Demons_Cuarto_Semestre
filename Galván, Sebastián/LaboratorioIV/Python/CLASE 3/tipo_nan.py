import math
from _pydecimal import Decimal

#NaN (Not a Number)
a = float('nan')
print(f'a: {a}')

#Modulo math
a = float('nan')
print(f'Es de tipo NaN(Not a Number)?: {math.isnan(a)}')

#Modulo Decimal
a = Decimal('nan')
print(f'Es de tipo NaN(Not a Number)?: {math.isnan(a)}')