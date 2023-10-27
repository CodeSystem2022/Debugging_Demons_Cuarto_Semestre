from capa_dato_persona import usuario
from capa_dato_persona.cursor_del_pool import CursorDelPool
from capa_dato_persona.usuario import Usuario
from logger_base import log

class UsuarioDAO:
    '''
    DAO significa: Data Access Object
    CRUD signidica:
                    Create -> Insertar
                    Read -> Seleccionar
                    Update -> Actualizar
                    Delete -> Eliminar
    '''
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username , passworld)VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s,passworld=%s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuario')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            log.debug(f'Persona insertada: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            log.debug(f'persona actualizada: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            log.debug(f'Los objetos eliminados son: {usuario}')
            valores = (usuario.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount


if __name__ == '__main__':

    # Eliminar un registro:
    usuario = Usuario(id_usuario=3)
    usuario_eliminado = UsuarioDAO.eliminar(usuario)
    log.debug(f' Usuario eliminado: {usuario_eliminado}')

    # Actualizar un registro
    usuario =Usuario(id_usuario=1,username='',password='369')
    usuario_modificado = UsuarioDAO.actualizar(usuario)
    log.debug(f'Usuario modificado: {usuario_modificado}')

    # Insertar un registro
    usuario = Usuario(username='Kely', password='321')
    usuario_insertado = UsuarioDAO.insertar(usuario)
    log.debug(f'Usuario insertado: {usuario_insertado}')

    # Seleccionar objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
