console.log("Hola a toda la coherte 2022");

var i = 0;

setInterval(function(){
    console.log(i);
    i++;

    if(i===5){
        console.log("Forzamos un error");
        var a = 3 + z;
    }
},1000);
console.log("Segunda intruccion")

// Node a diferencia de PHP, Python, Java, ES ASINCRONO, en tiempo de ejecucion va leyendo segun
// definicion, en cambio, los demas lenguajes mencionados si o si es de arriba hacia abajo respetando
// la jerarquia de ejecucion, node, se salta eso.