//===============CLASE 03 - MIERCOLES-31/08/2023===============
package utn.estudiantes.repositorio;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import utn.estudiantes.modelo.Estudiante;

@Repository
public interface EstudianteRepositorio extends JpaRepository<Estudiante, Integer>{

}
