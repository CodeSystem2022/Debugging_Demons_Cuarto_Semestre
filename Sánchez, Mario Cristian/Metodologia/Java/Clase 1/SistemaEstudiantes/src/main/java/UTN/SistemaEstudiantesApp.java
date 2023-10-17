package UTN;


import UTN.conexion.Conexion;
import UTN.datos.EstudianteDAO;
import UTN.dominio.Estudiante;

import java.util.Scanner;

public class SistemaEstudiantesApp {
    public static void main(String[] args) {
           var salir = false;
           var consola = new Scanner(System.in);
           //Se crea una instancia de la clase servicio, esto lo hacemos fuera del ciclo
           var estudianteDao = new EstudianteDAO();
           while (!salir){
               try{
                   mostrarMenu();
                   //Este sera el metodo que devolvera un booleano
                   salir = ejecutarOpciones(consola, estudianteDao); //Este arroja un exception
               }catch (Exception e){
                   System.out.println("Ocurrio un error al ejecutar la operacion: "+e.getMessage());
               }
           }
    }// Fin main

    private static void mostrarMenu(){
        System.out.println("""
                ******* Sistema de Estudiantes ****
                1. Listar Estudiantes
                2. Buscar Estudiantes
                3. Agregar Estudiantes
                4. Modificar Estudiante
                5. Eliminar Estudiante
                6. Salir
                Elige una opcion:
                """);
    } //Fin metodo mostrarMenu

    //Metodo para ejecutar las opciones, va a regresar un valor booleano ya que es el que puede
    //modificar el valor de la variable salir, si es verdadero termina el ciclo while
    private static boolean ejecutarOpciones(Scanner consola, EstudianteDAO estudianteDAO){
        var opcion = Integer.parseInt(consola.nextLine());
        var salir = false;
        switch (opcion){
            case 1 -> { //Listar estudiantes
                System.out.println("Listado Estudiantes...");
                //No muestra la informacion, solo recupera la info y regresa la lista
                var estudiantes = estudianteDAO.listarEstudiantes();//recibe el listado
                //Vamor a iterar cada objeto de tipo estudiante
                estudiantes.forEach(System.out::println); //Para imprimir la lista
            }//Fin caso 1

            case 2 -> { //Buscar estudiantes por id
                System.out.println("Introduce el id del estudiante a buscar: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                var estudiante = new Estudiante(idEstudiante);
                var encontrado = estudianteDAO.buscarEstudiantePorId(estudiante);
                if(encontrado)
                    System.out.println("Estudiante encontrado: "+estudiante);
                else
                    System.out.println("Estudiante no encontrado: "+estudiante);
            }//Fin caso 2

            case 3 -> { //Agregar un estudiante
                System.out.println("Agregar estudiante: ");
                System.out.println("Nombre: ");
                var nombre = consola.nextLine();
                System.out.println("Apellido: ");
                var apellido = consola.nextLine();
                System.out.println("Telefono: ");
                var telefono = consola.nextLine();
                System.out.println("Email: ");
                var email = consola.nextLine();
                //Crear objeto estudiante (sin id)
                var estudiante = new Estudiante(nombre, apellido, telefono, email);
                var agregado = estudianteDAO.agregarEstudiante(estudiante);
                if (agregado)
                    System.out.println("Estudiante agregado: "+agregado);
                else
                    System.out.println("Estudiante no agregado: "+agregado);
            }//Fin caso 3

            case 4 -> {//Modificar estudiante
                System.out.println("Modificar estudiante: ");
                //Aqui lo primero es especificar cual es el ID del objeto a modificar
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
                //Crea el objeto estudiante a modificar
                var estudiante = new Estudiante(idEstudiante, nombre, apellido, telefono, email);
                var modificado = estudianteDAO.modificarEstudiante(estudiante);
                if (modificado)
                    System.out.println("Estudiante modificado: "+estudiante);
                else
                    System.out.println("Estudiante no modificado: "+estudiante);

            }//Fin caso 4

            case 5 -> { //Eliminar estudiante
                System.out.println("Eliminar estudiante: ");
                System.out.println("ID estudiante: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                var estudiante = new Estudiante(idEstudiante);
                var eliminado = estudianteDAO.eliminarEstudiante(estudiante);
                if (eliminado)
                    System.out.println("Estudiante eliminado: "+estudiante);
                else
                    System.out.println("Estudiante no eliminado: "+estudiante);
            }//Fin caso 5

            case 6 -> {//Salir
                System.out.println("Nos vemos en Disney !!!");
                salir = true;
            }//Fin caso 6

            default -> System.out.println("Opcion no reconocida, ingrese otra opcion");
        }//Fin del switch

        return salir;
    }
}//Fin de clase