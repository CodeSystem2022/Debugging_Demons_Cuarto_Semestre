async function hola(nombre) {
    return new Promise(function (resolve, reject) {
        setTimeout(function () {
            console.log('Hola ' + nombre);
            resolve(nombre);
        }, 1000);
    })
}

async function hablar(nombre) {
    return new Promise( (resolve, reject) => { // usamos la sintaxis ES6
        setTimeout(function () {
            console.log('bla bla bla');
            resolve(nombre);
        }, 1000);
    });
}

//Función asincrona - adios
async function adios(nombre) {
    return new Promise((resolve, reject) => {
        setTimeout(function () {
            console.log('Adiós ' + nombre); //forma correcta de concatenar
            //resolve();
            reject('Hay un error');
        }, 1000);
    });
}

// await hola('Juani'); //--> Esto es una mala sintaxis

async function main(){
    let nombre = await hola('Gustavo');
    await hablar();
    await hablar();
    await hablar();
    await adios(nombre);
}
// En async-await lo que sucede por detras es convertir las promesas en procesos que se vean aparentemente como sincronos

main();
