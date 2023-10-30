#Dar formato a un string

nombre = 'Ariel'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre, edad) #CLASE 6-1

#Creamos una tupla
persona =('Carla','Gomez',5000.00)
mensaje_con_formato ='Hola %s %s . Tu sueldo es %.2f' # % persona #Aqui le pasamos el objeto que es la tupla
print(mensaje_con_formato % persona) #6-2

nombre = 'Juan'
edad = 19
sueldo = 3000
#mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre,edad,sueldo)

#mensaje = 'Nombre {0} Edad {1} sueldo {2:.2f}'.format(nombre,edad,sueldo)
#print(mensaje)

#mensasje = 'sueldo {2:.f} Edad {1} Nombre {0}'.format(nombre, edad, sueldo)
#print(mensaje)

mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
#print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad':Edad 35, 'sueldo':8000}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)


