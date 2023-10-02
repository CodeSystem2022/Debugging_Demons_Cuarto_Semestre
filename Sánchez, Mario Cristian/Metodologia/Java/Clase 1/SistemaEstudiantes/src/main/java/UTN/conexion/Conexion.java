package UTN.conexion;

import com.sun.jdi.connect.Connector;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexion {
    public static Connection getConnection(){
        Connection connexion = null;
        //Variables para conectarnos a la base de datos
        var baseDatos = "estudiantes";
        var url = "jdbc:mysql://localhost:3306/"+baseDatos;
        var usuario = "root";
        var password = "root";

        //cargamos la clse del driver de mysql en memoria
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connexion = DriverManager.getConnection(url, usuario, password);
        } catch (ClassNotFoundException | SQLException e){
            System.out.println("Ocurrio un error en la conexion: "+e.getMessage());
        }//Fin del catch

        return connexion;

    }//Fin metodo Connection
}
