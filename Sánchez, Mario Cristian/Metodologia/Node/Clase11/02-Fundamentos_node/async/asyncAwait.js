//La palabra Async no es necesaria en las funciones, por que ya son asincronas
//Igual proyectan una sincronia visual
async function hola(nombre) {
    return new Promise(function (resolve, reject){
        setTimeout(function () {
            console.log('Hola ' + nombre);
            resolve(nombre);
        }, 1000);   

    });
    
}

function hablar(nombre) {
    return new Promise((resolve, reject) => { //Usamos la sintaxis ES6
        setTimeout(function () {
            console.log('bla bla bla bla ')
            resolve(nombre);
            
        }, 1000)
    })
  
}

async function adios(nombre) {
    return new Promise((resolve, reject) => {
        setTimeout(function () {
            console.log('Adios ' + nombre);
            resolve();
           
        }, 1000);
    })
    
}

//await hola('Cristian'); Esto es una mala sintaxis
//await solo es valido denteo de una funcion asincrona
async function main() {
    let nombre = await hola('Cristian')
    await hablar();
    await hablar();
    await hablar();
    await adios(nombre);
    
console.log('Terminado el proceso...')
}

console.log('Empezamos el proceso...')
main();
console.log('Esta va a ser la segunda instruccion')