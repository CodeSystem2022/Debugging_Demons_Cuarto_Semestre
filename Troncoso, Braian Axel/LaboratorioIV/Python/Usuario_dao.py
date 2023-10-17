from conexion import Conexion
from cursor_del_pool import CursorDelPool
from Usuario import Usuario
from logger_base import log

class UsuarioDAO:
        """
    DAO significa: Data Acces Object
    CRUD significa:
        Create -> Insertar
        Read -> Seleccionar
        Update -> Actualizar
        Delete -> Eliminar
    """
        _SELECIONAR='SELECT * FROM usuario ORDER BY id_usuario'
        _INSERTAR='INSERT INTO usuario(username, password) VALUES (%s, %s)'
        _ACTUALIZAR='UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
        _ELIMINAR='DELETE FROM usuario WHERE id_usuario=%s'



        # Definimos los métodos de clase

        @classmethod
        def selecionar(cls):
            with CursorDelPool() as cursor:
                cursor.execute(cls._SELECIONAR)
                registros = cursor.fetchall()
                usuarios = [] # Creamos una lista
                for registro in registros:
                    usuario = Usuario(registro[0],registro[1],registro[2])
                    usuarios.append(usuario)
                return usuarios

        @classmethod
        def insertar(cls, usuario):
            with CursorDelPool() as cursor:
                valores = (usuario.username, usuario.password)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Usuario insertado: {usuario}')
                return cursor.rowcount


        @classmethod
        def actualizar(cls, usuario):
            with CursorDelPool() as cursor:
                valores = (usuario.username, usuario.password, usuario.id_usuario)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Usuario insertado: {usuario}')
                return cursor.rowcount

        @classmethod
        def eliminar(cls, usuario):
            with CursorDelPool() as cursor:
                valores = (usuario.id_usuario,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Usuario eliminado: {usuario}')
                return cursor.rowcount




if __name__ == '__main__':
    # Eliminar un registro
     usuario1 = Usuario(id_usuario=1)
     usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
     log.debug(f'Usuarios eliminados: {usuarios_eliminados}')

    # Actualizar un registro
     usuario1 = Usuario(1,'Juan', '891328132')
     usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
     log.debug(f'Usuarios actualizados: {usuarios_actualizados}')

    # Insertar un registro
     usuario1 = Usuario(username='Braian',password='Troncoso')
     usuarios_insertados = UsuarioDAO.insertar(usuario1)
     log.debug(f'Usuarios insertados: {usuarios_insertados}')

    # Selecionar objetos
usuarios = UsuarioDAO.selecionar()
for usuario in usuarios:
    log.debug(usuario)                