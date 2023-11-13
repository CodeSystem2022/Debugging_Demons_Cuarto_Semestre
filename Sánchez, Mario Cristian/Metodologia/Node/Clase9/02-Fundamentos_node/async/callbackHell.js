function hola(nombre, miCallBack) {
    setTimeout(function () {
        console.log('Hola ' + nombre);
        miCallBack(nombre);
    }, 1000);

}

function hablar(callbackHablar) {
    setTimeout(function () {
        console.log('bla bla bla bla ')
        callbackHablar();
    }, 1000)
}

function adios(nombre, otroCallBack) {
    setTimeout(function () {
        console.log('Adios ' + nombre);
        otroCallBack();
    }, 1000);
}


//Funcion recursiva
function conversacion(nombre, veces, callback) {
    if (veces > 0) {
        hablar(function () {
            conversacion(nombre, --veces, callback);
        });

    } else {
        callback(nombre, callback)
    }
}


//-- Proceso principal
console.log('Iniciando el proceso');
hola('Lauti', function (nombre) {
    conversacion(nombre, 4, function () {
        console.log('Terminando el proceso');
    })
});

// hola('Simon', function (nombre) {
//     hablar(function () {
//         hablar(function () {
//             hablar(function () {
//                 hablar(function () {
//                     adios(nombre, function () {
//                         console.log('Terminando el proceso');
//                     });
//                 });
//             });
//         });
//     });
// });

// hola('Simon', function(){});
// adios('Simon', function(){})
