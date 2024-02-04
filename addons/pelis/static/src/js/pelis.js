
// fichero para añadir el código javascript que necesitemos
// vamos a hacer lo necesario para que aparezca un console.log en la consola del navegador
// cuando se cargue la página
console.log('Hola desde Pelissss');

// mostrar un mensaje cuando la pagina se ha cargado 
$(document).ready(function () {


    console.log('La página se ha cargadosss');

    var car = document.querySelector('.cartelera');
    console.log('car', car);
    if (car != null) {
        car.addEventListener('click', function (e) {
            e.preventDefault();
            console.log('Has hecho click', e);
        });
    }
});









