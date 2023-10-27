// 3.1 Función flecha con template String: funcion asignada a una constante
const saludar = (nombre) =>{ // funcion de flecha que recibe un argumento
    return `Saludos de ${nombre}`; // usamos back tics con AltGr}
} // esto es igual a : 'Saludos' + nombre;

console.log(saludar('Giuliana'));