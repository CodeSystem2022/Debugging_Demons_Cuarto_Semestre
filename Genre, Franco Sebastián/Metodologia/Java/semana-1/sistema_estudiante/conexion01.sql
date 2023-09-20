-- Comenzamos con CRUD: create(insertar), read(leer), update(actualizar), delete(eliminar)
-- Listar los estudiantes (read)
SELECT * FROM estudiantes2022 order by idestudiantes2022;
-- Insertar estudiante
INSERT INTO estudiantes2022(nombre, apellido, telefono, email) VALUES ("Brian", "Lopez", "2604287985", "lopez@mail.com");
-- Update (modificar)
UPDATE estudiantes2022 SET nombre="Juan Carlos", apellido="Garcia" WHERE idestudiantes2022= 1;
-- Delete (eliminar)
DELETE FROM estudiantes2022 WHERE idestudiantes2022=8;
-- Para modificar el idestudiantes2022 y comience en 1
ALTER TABLE estudiantes2022 AUTO_INCREMENT = 1;
