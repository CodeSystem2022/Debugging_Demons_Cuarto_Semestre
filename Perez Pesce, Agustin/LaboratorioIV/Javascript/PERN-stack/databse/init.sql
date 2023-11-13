/* ===============CLASE 05 - LUNES-18/09/2023=============== */
CREATE TABLE tareas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) UNIQUE NOT NULL,
    descripcion TEXT,    
)
