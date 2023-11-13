# help(str.capitalize)
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()

print(f'mensaje1 {mensaje1}, id: {id(mensaje1)}')
print(f'mensaje2 {mensaje2}, id_ {id(mensaje2)}')

mensaje1 += ', adios'
print(f'mensaje1 {mensaje1}, id: {id(mensaje1)}')