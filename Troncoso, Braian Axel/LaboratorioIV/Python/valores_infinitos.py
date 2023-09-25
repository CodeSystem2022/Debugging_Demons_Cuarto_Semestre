import math
import decimal
# manejo de valores infinitos

infinito_positivo = float('inf')
print(f'infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
print(f'infinito negativo: {infinito_negativo}')
print(f'Es infinito): {math.isinf(infinito_negativo)}')

# Con el modulo math - usando el constructor
infinito_positivo = math.inf
print(f'infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(f'infinito negativo: {infinito_negativo}')
print(f'Es infinito): {math.isinf(infinito_negativo)}')

# Con el modulo decimal - usando el constructor
infinito_positivo = decimal('Infinity')
print(f'infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = decimal('-Infinity')
print(f'infinito negativo: {infinito_negativo}')
print(f'Es infinito): {math.isinf(infinito_negativo)}')