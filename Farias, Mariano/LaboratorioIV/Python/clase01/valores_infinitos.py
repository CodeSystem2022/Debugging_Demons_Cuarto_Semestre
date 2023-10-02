import math
from decimal import Decimal

#Manejo de valores infinitos
inifinito_positivo = float('inf')
print(f'Ifinito positivo: {inifinito_positivo}')
print(f'Es infinito?: {math.isinf(inifinito_positivo)}')

inifito_negativo = float('-inf')
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')

# Módulo math

inifinito_positivo = math.inf
print(f'ifinito positivo: {inifinito_positivo}')
print(f'Es infinito: {math.isinf(inifinito_positivo)}')

inifito_negativo = -math.inf
print(f'Infinito negativo: {infinito_negativo}')
print(f'infinito?: {math.isinf(inifito_negativo)}')

# Módulo decimal
inifinito_positivo = Decimal('Infinity')
print(f'ifinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

inifinito_negativo = Decimal('-Infinity')
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')

