//===============CLASE 07 - MIERCOLES-27/09/2023===============
package utn.tienda_libros.repositorio;


import org.springframework.data.jpa.repository.JpaRepository;
import utn.tienda_libros.modelo.Libro;

public interface LibroRepositorio extends JpaRepository<Libro, Integer> {

}
