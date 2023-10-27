from Usuario import Usuario
from cursor_del_pool import CursorDelPool
from logger_base import log

class UsuarioDAO:

    '''
    DAO -> Data Access Object para la tabla de ususarios
    CRUD -> Create - Read - Update - Delete
    '''

    _SELECT = 'SELECT * FROM users ORDERBY id'
    _INSERTAR= 'INSERT INTO users(username, password) VALUE (%s,%s)'
    _ACTUALIZAR = 'UPDATE users SET username=%s, password=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM users WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as curor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append([usuario])
            return  usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
                log.debug(f'Usuario a eliminar: {usuario}')
                valores = (usuario.id_usuario,)
                cursor.execute(cls._ELIMINAR, valores)
                cursor.rowcount


if __name__ == '__main__':



