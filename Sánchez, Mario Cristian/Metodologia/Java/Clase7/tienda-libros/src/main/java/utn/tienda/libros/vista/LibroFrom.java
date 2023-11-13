package utn.tienda.libros.vista;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import utn.tienda.libros.servicio.LibroServicio;

import javax.swing.*;

@Service
public class LibroFrom extends JFrame {
    LibroServicio libroServicio;
    private JPanel panel;

    @Autowired
    public LibroFrom(LibroServicio libroServicio){
        this.libroServicio = libroServicio;
        iniciarForma();
    }

    private void iniciarForma(){
        setContentPane(panel);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        setSize(900, 700);
    }
}
