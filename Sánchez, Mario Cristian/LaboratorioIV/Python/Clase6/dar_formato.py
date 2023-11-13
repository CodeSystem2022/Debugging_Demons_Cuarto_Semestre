# Dar formato a un string

nombre = "Lautaro"
edad = 8
mensaje_con_formato = 'Mi nombre es %s y tengo  %d años' %(nombre, edad)
print(mensaje_con_formato)

# Creamos una tupla
persona = ('Carla', 'Gomez', 5000.00)
mensaje_con_formato = 'Hola  %s %s . Tu sueldo es %.2f '  # % persona  <= Aqui le pasamos el objeto que es una tupla
print(mensaje_con_formato % persona)


# Metodo format
nombre = 'Juan'
edad = 19
sueldo = 3000
mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje = 'Sueldo {2:.2f} Edad {1} Nombre {0} '.format(nombre, edad, sueldo)
print(mensaje)


mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad': 35, 'sueldo': 8000.00}
mensaje = 'Nombre {persona[nombre]} Edad {persona[edad]} sueldo {persona[sueldo]:.2f}'.format(persona=diccionario)
print(mensaje)



















