# Dar formato a un string
nombre = 'Pablo'
edad = 30
mensaje_con_formato = 'Mi nombre es %s y tengo  %d años '% (nombre,edad)
#Creamos una tupla
persona =('Carlos','Gomez',5000.00)
mensaje_con_formato = 'Hola %s %s . Tu sueldo es %.2f' # %persona # Aqui le pasamos el objeto que es tupla
#print(mensaje_con_formato % persona)

nombre = 'Juan'
edad = 19
sueldo = 3000
#mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre,edad,sueldo)
#print(mensaje_con_formato)
mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre,edad,sueldo)
print(mensaje)
