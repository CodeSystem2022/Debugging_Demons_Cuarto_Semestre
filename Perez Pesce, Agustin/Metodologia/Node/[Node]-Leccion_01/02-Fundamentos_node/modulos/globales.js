// this === global = true

// mostrar algo en consola
// console.log();

// mostrar un mensaje en forma de error
// console.error();

// ejecutar código despues de un intervalo de tiempo
// setTimeout(() =>{});

// ejecutar un código cada intervalo de tiempo
// setInterval(()=>{});

// da prioridad de ejecución a una función asincronica

// console.log(global)
// console.log(setInterval)

let i = 0;
let intervalo = setInterval(()=>{
    console.log('Hola');
    if(i === 3){
        clearInterval(intervalo); // Detenemos la función
    }
    i++;
},1000);


setImmediate(()=>{
    console.log('Saludo inmediato')
});

// requiere();

// console.log(process);

// console.log(__direname);

// console.log(__filename);

global.miVariable = 'Mi variable Global';

console.log(miVariable);