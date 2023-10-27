console.log('Inicio del programa '); //1

setTimeout(() => {
    console.log('primer TimeOut') //3
}, 1000); // Tiempo luego de la coma y llave.  


setTimeout(() => {
    console.log('Segundo TimeOut') //4
}, 2000); // Tiempo luego de la coma y llave.

setTimeout(() => {
    console.log('Tercero TimeOut') //5
}, 3000); // Tiempo luego de la coma y llave.

console.log('Fin De programa');  //2
