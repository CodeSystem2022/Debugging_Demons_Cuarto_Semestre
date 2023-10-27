from Usuario import Usuario
from usuario_dao import UsuarioDAO
from logger_base import log

opcion = None
while opcion != 5:
    print('Opciones: ')
    print('1. Listar Usuarios')
    print('2. Agregra Usuarios')
    print('3. Modificar Usuarios')
    print('4. Eliminar Usuarios')
    print('5. Salir')
    opcion = int(input('Ingrese una opcion (1 - 5 ): '))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Ingrese nombre de usuario: ')
        password_var = input('Ingrese password: ')
        usuario = Usuario(username= username_var, password=password_var)
        username_insertado  =UsuarioDAO.insertar(usuario)
        log.info(f'Usuario insertado: {username_insertado}')
    elif opcion == 3:
        id_usuario_var = int(input('Ingrese el id del usuario a modificar: '))
        username_var = input('Ingrese nuevo username: ')
        password_var = input('Ingrese nueva contraseña: ')
        usuario = Usuario(id=id_usuario_var, username=username_var, password=password_var)
        username_actualizado = UsuarioDAO.actualizar(username_actualizado)
        log.info(f'Usuario actualizado: {username_actualizado}')
    elif opcion == 4:
        id_usuario_var = int(input('Ingrese id de usuario a eliminar'))
        usuario = Usuario(id=id_usuario_var)
        username_eliminado = UsuarioDAO.eliminar(usuario)
        log.info(f'Ususario eliminado: {username_eliminado}')
else:
    log.info('Saliendo de la aplicacion...')