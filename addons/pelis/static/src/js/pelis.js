 
    // fichero para añadir el código javascript que necesitemos
    // en este caso, añadimos un evento click a un botón
    // que al pulsarlo, muestra un mensaje en la consola del navegador
    // y un mensaje en un alert
    $(document).ready(function() {
        $('#button').click(function() {
            console.log('Button clicked');
        });
    });
