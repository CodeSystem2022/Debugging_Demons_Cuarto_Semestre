help(str.split)

cursos = 'Java Javascript Node Python Diseño'
lista_cursos = cursos.split()
print(f'Lista de cusros: {lista_cursos}')
print(type(lista_cursos))

cursos_separados_coma = 'Java, Python, GO, Javascript, PHP'
lista_cursos = cursos_separados_coma.split(',', 2)
print(f'Lista de cusros: {lista_cursos}')
print(len(lista_cursos))