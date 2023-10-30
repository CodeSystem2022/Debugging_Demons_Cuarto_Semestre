
help(str.split)

cursos = 'JavaScrip Node Python Diseño'
lista_cursos = cursos.split()
print(f'Lista de cursos: {lista_cursos}')
print(type(lista_cursos))

cursos_separados_coma ='java,Python,Nose,JavaScrip,Spring'
lista_cursos = cursos_separados_coma.split(',',2)
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos))
#CLASE 5 TERMINADA