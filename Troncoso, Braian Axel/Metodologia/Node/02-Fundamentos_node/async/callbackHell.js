function hola(nombre, miCallBack){
    setTimeout(function (){
        console.log('Hola, '+nombre);
        miCallBack(nombre);
    },1000);
}

function hablar(callbackHablar){
    setTimeout(function (){
        console.log('bla bla bla')
        callbackHablar();
    },1000);
}

function adios(nombre, otraCallback){
    setTimeout(function(){
        console.log('Adios '+ nombre);
        otraCallback();
    },1500)
}

//-- Funcion recursiva
function conversacion(nombre, veces, callback){
    if(veces > 0){
        hablar(function() {
            conversacion(nombre, --veces, callback);
        });
    }else{
        callback(nombre, callback);
    }
}

//-- Proceso Princial
console.log('Iniciando el proceso...');
hola('Ariel',function(nombre){
    conversacion(nombre, 4, function(){
        console.log('Terminamos el proceso...')
    })
})
// hola('Carlos',function(nombre){
//     hablar(function (){
//         hablar(function (){
//             hablar(function (){
//                 hablar(function (){
//                     hablar(function (){
//                         adios(nombre,function(){
//                             console.log('Finalizando el proceso...')
//                             adios(nombre,function(){
//                                 console.log('Finalizando el proceso...')
//                             });
//                         });
//                     });
//                 });
//             }); 
//         });
//     });
// });