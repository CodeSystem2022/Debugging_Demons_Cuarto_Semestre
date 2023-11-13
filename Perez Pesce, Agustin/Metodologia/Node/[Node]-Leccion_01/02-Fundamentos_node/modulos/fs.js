const fs = require('fs');

// Primero leemos el archivo.txt

function leer(ruta, cb){
    fs.readFile(ruta,(err, data)=>{
        cb(data.toString());
    })
}

function escribir(ruta, contenido){
    fs.writeFile(ruta, contenido, function(err){
        if(err){
            console.log('No se ha podido escribir :(',err);
        }else{
            console.log('Se ha escrito correctamente :D');
        }
    })
}
// Tercero eliminamos el archivo1.txt
function borrar(ruta,cb){
    fs.unlink(ruta,cb); // Elimina de manera asincrona
    // Es unlink porque asi se hacia referencia cuando no borra de manera directa sino su referencia en memoria
    // Por eso no utilizamos delete
}

//borrar(`${__dirname}/archivo1.txt`,console.log);
//escribir(`${__dirname}/archivo1.txt`,'Soy un nuevo archivo', console.log) // La funcion writeFile lo que hace
// Es sobre escribir el archivo en el cual escribe, si le paso una leyenda esta misma sobreescribira la que estaba anteriormente.
//leer(`${__dirname}/archivo.txt`,console.log); // Sintaxis ES6

