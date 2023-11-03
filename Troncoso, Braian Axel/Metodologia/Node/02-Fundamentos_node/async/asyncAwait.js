// La palabra async NO ES necesarias en las funciones porqué ya son asincronas
// Igual proyectan una sincrona visual
async function hola(nombre){ // async puede trabajar sin la necesidad de utilizar el await
    return new Promise(function (resolve, reject) {
        setTimeout(function (){
            console.log('Hola, '+nombre);
            resolve(nombre);
        },1000);
    });
   
}

async function hablar(nombre){
    return new Promise((resolve,reject) =>{ // Usamos la sintaxis de ES6
        setTimeout(function (){
            console.log('bla bla bla')
            resolve(nombre);
        },1000);
    })
}

async function adios(nombre){
    return new Promise((resolve, reject)=>{
        setTimeout(function(){
            console.log('Adios '+ nombre);
            resolve();
            // reject('Hay un error');
        },1500)
    })
}

// await hola('Ariel'); // Esto es una mala sintaxis, no sabe que hacer
// await solo es valido dentro de una funcion asincrona
// Se puede usar async sin el await pero await no se puede usar sin el async
async function main(){
    let nombre = await hola('Ariel')
    await hablar()
    await hablar()
    await hablar()
    await hablar()
    await adios(nombre)
    console.log('Termina el proceso...')
};
console.log('Empezamos el proceso...')
main();
console.log('Esta va ser la segunda instrucción')