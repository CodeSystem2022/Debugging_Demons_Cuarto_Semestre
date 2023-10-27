package UTN.datos;

import UTN.dominio.Estudiante;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import static UTN.conexion.Conexion.getConnection;

public class EstudianteDAO {

    public List<Estudiante> listar() {
        List<Estudiante> estudiantes = new ArrayList<>();
        PreparedStatement ps; 
        ResultSet rs; 

     
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022;";


        try {
            ps = con.prepareStatement(sql); 
            rs = ps.executeQuery(); 
            while (rs.next()) {
                
                Estudiante estudiante = new Estudiante();
                estudiante.setIdEstudiante(rs.getInt("idestudiantes2022"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                
                estudiantes.add(estudiante);
            }
        } catch (Exception e) {
            System.out.println("Ocurrió un error al listar datos: " + e.getMessage());
        } finally {
           
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Ocurrió un error al cerrar la conexión: " + e.getMessage());
            }
        } 
        return estudiantes;
    } 
 
    public boolean buscarPorId(Estudiante estudiante) {
        PreparedStatement ps; 
        ResultSet rs;

        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022 WHERE idestudiantes2022 =?;";

        try {
            ps = con.prepareStatement(sql); 
            ps.setInt(1, estudiante.getIdEstudiante());
            rs = ps.executeQuery(); 
            if (rs.next()) {

                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                return true;

            }
        } catch (Exception e) {
            System.out.println("Ocurrió un error al buscar por Id: " + e.getMessage());
        } finally {
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Ocurrió un error al cerrar la conexión: " + e.getMessage());
            }
        }
        return false;
    }

    public boolean agregarEstudiante(Estudiante estudiante) {
        PreparedStatement ps; 
        Connection con = getConnection();
        String sql = "INSERT INTO estudiantes2022 (nombre, apellido, telefono, email) VALUES (?,?,?,?);";
        try {
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());

            ps.execute();
            return true;
        } catch (Exception e) {
            System.out.println("Ocurrió un error al agregar un estudiante: " + e.getMessage());
        } finally {
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Ocurrió un error al cerrar la conexión: " + e.getMessage());
            }
        }
        return false;
    }

    public boolean modificarEstudiante(Estudiante estudiante) {
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "UPDATE estudiantes2022 SET nombre = ?, apellido = ? , telefono = ? , email = ? WHERE idestudiantes2022 = ?;";
        try {
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.setInt(5, estudiante.getIdEstudiante());

            ps.execute();
            return true;
        } catch (Exception e) {
            System.out.println("Ocurrió un error al modificar un estudiante: " + e.getMessage());
        } finally {
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Ocurrió un error al cerrar la conexión: " + e.getMessage());
            }
        }
        return false;
    }

    public boolean eliminarEstudiante(Estudiante estudiante) {
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "DELETE FROM estudiantes2022 WHERE idestudiantes2022 = ?;";
        try {
            ps = con.prepareStatement(sql); 
            ps.setInt(1, estudiante.getIdEstudiante());
            ps.execute();
            return true;
        } catch (Exception e) {
            System.out.println("Ocurrió un error al eliminar un estudiante: " + e.getMessage());
        } finally {
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Ocurrió un error al cerrar la conexión: " + e.getMessage());
            }
        } 
        return false;

    }

    public static void main(String[] args) {
        EstudianteDAO estudianteDAO = new EstudianteDAO();
        System.out.println("Listado de estudiantes: ");
        List<Estudiante> estudiantes = estudianteDAO.listar();
        estudiantes.forEach(System.out::println);

        System.out.println("Buscamos por id: ");
        Estudiante estudiante1 = new Estudiante(3);
        Boolean resultado = estudianteDAO.buscarPorId(estudiante1);
        if (resultado) {
            System.out.println("Estudiante encontrado: ");
            System.out.println(estudiante1);
        } else {
            System.out.println("Estudiante no encontrado. Id: " + estudiante1.getIdEstudiante());
        }

    } 
}