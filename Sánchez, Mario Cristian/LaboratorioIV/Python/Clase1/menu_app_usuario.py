from capa_datos_persona.Usuario import Usuario
from capa_datos_persona.usuario_dao import UsuarioDAO
from logger_base import log

opcion = None
while opcion != 5:
    print('Opciones: ')
    print('1. Listar Usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Digite la opcion entre 1 a 5: '))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Digite el nombre de usuario: ')
        password_var = input('Digite su contraseña: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuario_insertado = UsuarioDAO.insertar(usuario)
        log.info(f'Usuario insertado: {usuario_insertado}')
    elif opcion == 3:
        id_usuario_var = int(input('Digite el ID del usuario a modificar: '))
        username_var = input(f'Digite el nombre del usuario a modificar: ')
        password_var = input(f'Digite el passsword a modificar : ')
        usuario = Usuario(id_usuario=id_usuario_var, username=username_var, password= password_var)
        usuario_modificado = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuario actualizado: {usuario_modificado}')
    elif opcion == 4:
        id_usuario_var = input('Digite el ID del usuario a eliminar: ')
        usuario = Usuario(id_usuario=id_usuario_var)
        usuario_eliminado = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuario_eliminado}')

else:
     log.info('Salimos de la aplicacion, Hasta pronto!!!')
