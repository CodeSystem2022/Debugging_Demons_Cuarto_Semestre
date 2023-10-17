package utn.estudiantes.servicio;

import utn.estudiantes.modelo.Estudiante;

import java.util.List;

public interface IServicioEstudiante {
    public List<Estudiante> listarEstudiantes();
    public Estudiante buscarEstudiantePorId(Integer idEstudiante);
    public void agregarEstudiante(Estudiante estudiante);
    public void eliminarEstudiante(Estudiante estudiante);
}
