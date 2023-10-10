from Usuario_dao import UsuarioDAO
from logger_base import log
from Usuario import Usuario
opcion = None

while opcion != 5:
    print('Opciones: ')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Digite una opción del (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDAO.selecionar()
        for usuario in usuarios:
            log.info(usuario)

    elif opcion == 2:
        username_var = input('Inserte el username: ')
        password_var = input('Inserte el password: ')
        usuario = Usuario(username = username_var, password= password_var)
        usuario_insertado = UsuarioDAO.insertar(usuario)
        log.info(f'Usuario insertado correctamente: {usuario_insertado}')

    elif opcion == 3:
        id_usuario_var  = int(input('Digite el ID del usuario a modificar: '))
        username_var = int(input('Digite el nombre del usuario a modificar: '))
        password_var = int(input('Digite la contraseña del usuario a modificar: '))

        usuario = Usuario(id_usuario=id_usuario_var, username=username_var, password= password_var)
        usuario_actualizado = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuario modificado {usuario_actualizado}')

    elif opcion == 4:
        id_usuario_var = int(input('Digite el ID del usuaro a eliminar: '))

        usuario = Usuario(id_usuario=id_usuario_var)
        usuario_eliminado = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuario_eliminado}')

else:
    log.info('Salimos de la aplicación, Hasta pronto')

