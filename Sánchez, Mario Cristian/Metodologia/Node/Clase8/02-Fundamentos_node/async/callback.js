function hola(nombre, miCallBack){
    setTimeout(function () {
        console.log('Hola '+nombre);
        miCallBack(nombre);
    },1000);
    
}

function adios(nombre, otroCallBack) {
    setTimeout( function() {
        console.log('Adios '+ nombre);
        otroCallBack();
    }, 1000);
}

console.log('Iniciando el proceso');

hola('Simon', function(nombre){
    adios(nombre , function(){
        console.log('Terminando el proceso');
    });
    
});

// hola('Simon', function(){});
// adios('Simon', function(){});
