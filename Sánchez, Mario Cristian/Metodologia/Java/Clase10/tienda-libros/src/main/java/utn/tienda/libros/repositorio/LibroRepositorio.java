package utn.tienda.libros.repositorio;

import org.springframework.data.jpa.repository.JpaRepository;
import utn.tienda.libros.modelo.Libro;

public interface LibroRepositorio  extends JpaRepository<Libro, Integer> {

}
