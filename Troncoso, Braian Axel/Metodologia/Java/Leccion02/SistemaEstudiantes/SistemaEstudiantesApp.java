package UTN.Presentacion;

import UTN.Conexion.Conexion;
import UTN.Datos.EstudianteDAO;
import UTN.Dominio.Estudiante;

import java.util.Scanner;

public class SistemaEstudiantesApp {
    public static void main(String[] args) {
        /*   var conexion = Conexion.getConecction();
        if (conexion != null){
            System.out.println("Conexión exitosa: "+conexion);
        }else {
            System.out.println("Error al conectarse");
        }
        */
        var salir = false; // Recuerden esto ya lo hicimos antes
        var consola = new Scanner(System.in); // Para leer informacion de la consola
        // Se crea una instancia de la clase servicio, esto lo hacemos fuera del ciclo
        var estudianteDao = new EstudianteDAO();
        while (!salir){
            try {
                mostrarMenu(); // Mostramos el menu
                // Esté sera el método ejecutarOpciones que devolverá un booleano
                salir = ejecutarOpciones(consola, estudianteDao); // Esto arroja una excepcion
            } catch (Exception e){
                System.out.println("Ocurrió un error al ejecutar la operacion: "+ e.getMessage());
            }
        } // Fin while
    }// Fin main

    private static void mostrarMenu(){
        System.out.println("""
    *** Sistema de estudiantes ***
    1. Listar estudiantes
    2. Buscar estudiante
    3. Agregar estudiante
    4. Modificar estudiante
    5. Eliminar estudiante
    6. Salir
    Elige una opcion: 
    """);
    }
// Método para ejecutar las opciones, va a regresar un valor boolean, ya que es el que
        // Puede modificar el valor de la variable salir, si es verdadero termina el ciclo whiel
    private static boolean ejecutarOpciones(Scanner consola, EstudianteDAO estudianteDAO){
            var opcion = Integer.parseInt(consola.nextLine());
            var salir = false;
            switch (opcion){
                case 1 -> { // Listar estudiantes
                    System.out.println("Listado de estudiantes...");
                    // no muestra la informacion, esto recupera la info y regresa una lista
                    var estudiantes = estudianteDAO.listarEstudiantes(); // Recibe el listado
                    // Vamos a iterar cada objeto de tipo estudiante
                    estudiantes.forEach(System.out::println); //para imprimir la lista
                }//Fin caso 1
                case 2 ->{ // Buscar estudiante por id
                    System.out.println("Introduce el id_estudiante a buscar: ");
                    var idEstudiante = Integer.parseInt(consola.nextLine());
                    var estudiante = new Estudiante(idEstudiante);
                    var encontrado = estudianteDAO.buscarEstudiantePorId(estudiante);
                    if (encontrado)
                        System.out.println("Estudiante encontrado: "+estudiante);
                    else
                        System.out.printf("Estudiante NO encontrado "+estudiante);
                }// Fin caso 2
                case 3 ->{ // Agregar estudiante
                    System.out.println("Agregar estudiante: ");
                    System.out.println("Nombre: ");
                    var nombre = consola.nextLine();
                    System.out.println("Apellido: ");
                    var apellido = consola.nextLine();
                    System.out.println("Telefono: ");
                    var telefono = consola.nextLine();
                    System.out.println("Email: ");
                    var email = consola.nextLine();
                    // Crear objeto estudiante(sin id)
                    var estudiante = new Estudiante(nombre,apellido,telefono,email);
                    var agregado = estudianteDAO.agregarEstudiante(estudiante);
                    if (agregado)
                        System.out.println("Estudiante agregado: "+estudiante);
                    else
                        System.out.println("Estudiante NO agregado: "+estudiante);
                }// Fin caso 3
                case 4 ->{ // Modificar estudiante
                    System.out.println("Modificar estudiante: ");
                    // Aqui lo primero es especificar el cuál es el id del objeto a modificar
                    System.out.println("Id Estudiante: ");
                    var idEstudiante = Integer.parseInt(consola.nextLine());
                    System.out.println("Nombre: ");
                    var nombre = consola.nextLine();
                    System.out.println("Apellido: ");
                    var apellido = consola.nextLine();
                    System.out.println("Telefono: ");
                    var telefono = consola.nextLine();
                    System.out.println("Email: ");
                    var email = consola.nextLine();
                    // Crear objeto estudiante(con id)
                    var estudiante = new Estudiante(idEstudiante,nombre,apellido,telefono,email);
                    var modificado = estudianteDAO.modificarEstudiante(estudiante);
                    if (modificado)
                        System.out.println("Estudiante modificado: "+ estudiante);
                    else
                        System.out.println("Estudiante NO modificado: "+ estudiante);
                }// Fin caso 4
                case 5 -> { // Eliminar estudiante
                    System.out.println("Eliminar estudiante: ");
                    System.out.println("Id Estudiante: ");
                    var idEstudiante = Integer.parseInt(consola.nextLine());
                    var estudiante = new Estudiante(idEstudiante);
                    var eliminado = estudianteDAO.eliminarEstudiante(estudiante);
                    if (eliminado)
                        System.out.println("Estudiante eliminado: "+ estudiante);
                    else
                        System.out.println("Estudiante NO eliminado: "+ estudiante);

                }// Fin caso 5
                case 6 ->{ // Salir
                    System.out.println("Hasta pronto!!!");
                    salir = true;
                }// Fin caso 6
                default -> System.out.println("Opción no reconocida, ingrese otra opción");
            } // Fin switch
return salir;
    }
}// Fin clase
