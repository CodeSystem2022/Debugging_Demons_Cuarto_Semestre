console.log('Inicio del programa'); //1
setTimeout(() => {
    console.log('Primer Timeout'); //5
}, 30000);

setTimeout(() => {
    console.log('Segundo Timeout'); //2
}, 0);

setTimeout(() => {
    console.log('Tercero Timeout'); //3
}, 0);

console.log('Fin del programa'); //4