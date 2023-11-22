// Variables para el contador
let contador = 0;

// Función para incrementar el contador
function incrementarContador() {
contador++;
actualizarContador();
}

// Función para decrementar el contador
function decrementarContador() {
if (contador > 0) {
    contador--;
    actualizarContador();
}
}

// Función para resetear el contador
function resetearContador() {
contador = 0;
actualizarContador();
}

// Función para actualizar el elemento HTML que muestra el contador
function actualizarContador() {
document.getElementById('contador').innerText = contador;
}
