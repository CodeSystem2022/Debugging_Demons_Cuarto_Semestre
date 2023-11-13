import math
from decimal import Decimal
# NaN 8Not a Number)
a = float('NaN')
print(f'a: {a}')

# Modulo math
a = float('NaN') #NaN es un numero
print(f'Es de tipo de NaN?: {math.isnan(a)}')

# Modulo Decimal
a = Decimal('nan')
print(f'Es de tipo de NaN?: {math.isnan(a)}')