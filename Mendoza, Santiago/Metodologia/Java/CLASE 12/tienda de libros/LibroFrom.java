package utn.tienda_libros.vista;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import utn.tienda_libros.modelos.Libro;
import utn.tienda_libros.servicio.LibroServicio;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

@Component
public class LibroFrom extends JFrame  {
    LibroServicio libroServicio;
    private JPanel panel;
    private JTable tablaLibros;
    private JTextField idTexto;
    private JTextField libroTexto;
    private JLabel Autor;
    private JTextField autorTexto;
    private JTextField precioTexto;
    private JTextField existenciasTexto;
    private JButton agregarButton;
    private JButton modificarButton;
    private JButton eliminarButton;
    private DefaultTableModel tablaModeloLibros;


    @Autowired
    public LibroFrom(LibroServicio libroServicio){
        this.libroServicio = libroServicio;
        iniciarForma();
        agregarButton.addActionListener(e -> agregarLibro());{

        };
        tablaLibros.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                super.mouseClicked(e);
                cargarLibroSeleccionado();
            }
        });
        modificarButton.addActionListener(e -> modificarLibro());
        eliminarButton.addActionListener(e -> eliminarLibro());
    }

    private void eliminarLibro() {
        var renglon = tablaLibros.getSelectedRow();
        if (renglon != -1){
            String idLibro = tablaLibros.getModel().getValueAt(renglon, 0).toString();
            var libro = new Libro();
            libro.setIdLibro(Integer.parseInt(idLibro));
            libroServicio.eliminarLibro(libro);
            mostrarMensaje("Libro "+idLibro+" ELIMINADO");
            limpiarFormulario();
            listarLibros();
        }else{
            mostrarMensaje("No se ha seleccionado ningun libro de la Tabla a Eliminar");
        }
    }

    private void iniciarForma() {
        setContentPane(panel);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        setSize(900,700);
        // Para obtener las dimenciones de la ventana
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension tamanioPantalla = toolkit.getScreenSize();
        int x = (tamanioPantalla.width - getWidth() / 2);
        int y = (tamanioPantalla.height - getHeight() / 2);
        setLocation(x,y);
    }

    public void agregarLibro(){
        // Leer los valores del formulario
        if (libroTexto.getText().equals("")){
            mostrarMensaje("Ingrese el nombre del libro");
            libroTexto.requestFocusInWindow();
            return;
        };
        var nombreLibro = libroTexto.getText();
        var autor = autorTexto.getText();
        var precio = Double.parseDouble(precioTexto.getText());
        var existencias = Integer.parseInt(existenciasTexto.getText());
        // Si pasamos el valor null va hacer un INSERT en caso que le pasemos un ID va a ser un UPDATE
        var libro = new Libro(null,nombreLibro,autor,precio,existencias);
          /*  libro.setNombreLibro(nombreLibro);
            libro.setAutor(autor);
            libro.setPrecio(precio);
            libro.setExistencias(existencias);*/
        this.libroServicio.guardarLibro(libro);
        mostrarMensaje("Se agregó el libro");
        limpiarFormulario();
        listarLibros();
    };

    private void cargarLibroSeleccionado() {
        // Los indices de las columnas inician en 0
  var renglon = tablaLibros.getSelectedRow();
  if(renglon != -1){
      String idLibro = tablaLibros.getModel().getValueAt(renglon, 0).toString();
      idTexto.setText(idLibro);

      String nombreLibro = tablaLibros.getModel().getValueAt(renglon,1).toString();
      libroTexto.setText(nombreLibro);

      String autor = tablaLibros.getModel().getValueAt(renglon,2).toString();
      autorTexto.setText(autor);

      String precio = tablaLibros.getModel().getValueAt(renglon,3).toString();
      precioTexto.setText(precio);

      String existencias = tablaLibros.getModel().getValueAt(renglon,4).toString();
      existenciasTexto.setText(existencias);

  }
    }

    private void modificarLibro() {
    if (this.idTexto.equals("")){
        mostrarMensaje("Debes seleccionar un Registro en la Tabla");
    }else{
        // Verificamos que él nombre del libro no sea nulo
        if (this.libroTexto.equals("")){
            mostrarMensaje("Digite el nombre del Libro...");
            libroTexto.requestFocusInWindow();
            return;
        }if (this.libroTexto == this.libroTexto){
            mostrarMensaje("No se ha modificado NADA");
            libroTexto.requestFocusInWindow();
            return;
        }
        else {
            mostrarMensaje("No se  ha seleccionado NINGUN Libro para Modificar");
        }
        // Llenamos el objeto Libro a actualizar
        int idLibro = Integer.parseInt(idTexto.getText());
        var nombreLibro = libroTexto.getText();
        var autor = autorTexto.getText();
        var precio = Double.parseDouble(precioTexto.getText());
        var existencias = Integer.parseInt(existenciasTexto.getText());
        var libro = new Libro(idLibro,nombreLibro,autor,precio,existencias);
        libroServicio.guardarLibro(libro);
        mostrarMensaje("Se modificó el Libro");
        limpiarFormulario();
        listarLibros();
    }
    }

    private void limpiarFormulario(){
        libroTexto.setText("");
        autorTexto.setText("");
        precioTexto.setText("");
        existenciasTexto.setText("");
    };

    private void mostrarMensaje(String mensaje){
        JOptionPane.showMessageDialog(this,mensaje);
    };

    private void listarLibros() {
        // Limpiamos la tabla
        tablaModeloLibros.setRowCount(0);

        // Obtenemos los libros de la base datos
        var libros = libroServicio.listarLibros();

        //  Iteramos cada libro
        libros.forEach((libro)->{
            // Creamos cada registro para agregarlos a la tabla
            Object [] reglonLibro = {
                    libro.getIdLibro(),
                    libro.getNombreLibro(),
                    libro.getAutor(),
                    libro.getPrecio(),
                    libro.getExistencias()
            };
            this.tablaModeloLibros.addRow(reglonLibro);
        });

    }
    // Como intectamos una instancia de LibroServicio en nuestro constructor de la clase LibroForms, ya podriamos utilizar esa instancia
    // en cualquier parte de nuestra clase
    private void createUIComponents() {
        idTexto = new JTextField("");
        idTexto.setVisible(false);
        this.tablaModeloLibros = new DefaultTableModel(0 , 5){
            @Override
            public boolean isCellEditable(int row, int column){
                return false;
            }
        };
        String [] cabecera = {"Id", "Libro", "Autor", "Precio", "Existencias"};
        this.tablaModeloLibros.setColumnIdentifiers(cabecera);
        // Instanciar el objeto de Jtable
        this.tablaLibros = new JTable(tablaModeloLibros);
        // Evitamos que se seleccionen varios registros a la vez
        tablaLibros.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        listarLibros();
    }
}
