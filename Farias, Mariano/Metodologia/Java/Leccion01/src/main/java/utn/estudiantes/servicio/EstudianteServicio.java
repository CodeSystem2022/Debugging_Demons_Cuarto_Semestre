package utn.estudiantes.servicio;

import utn.estudiantes.modelo.Estudiante;

import java.util.List;

public class EstudianteServicio implements IEstuadinateServicio {
    public List<Estudiante> ListarEstudiantes();
    public Estudiante buscarEstudiantePorId(Integer idEstudiante);
    public void guardarEstudiante(Estudiante estudiante);
    public void eliminarEstudiantes(Estudiante estudiante);
}
