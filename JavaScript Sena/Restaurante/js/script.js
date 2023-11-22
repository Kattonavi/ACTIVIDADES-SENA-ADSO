// Definición de los precios de los productos
const precios = {
    bandejaPaisa: 15000,
    ajiaco: 12000,
    empanadas: 2000,
    aguapanela: 3000,
    jugoLulo: 2500,
    tinto: 800,
    platoEjecutivo: 20000, // Precio del plato ejecutivo
};

// Función para calcular el total del pedido
function calcularTotal() {
    // Obtener elementos del formulario
    const platoSeleccionado = document.getElementById("platos").value;
    const bebidaSeleccionada = document.getElementById("bebidas").value;
    const platoEjecutivo = document.getElementById("platoEjecutivo").checked;
    const cantidadPlatos = parseInt(document.getElementById("cantidadPlatos").value);
    const cantidadBebidas = parseInt(document.getElementById("cantidadBebidas").value);

    // Elementos de la página para mostrar el pedido y el total
    const pedido = document.getElementById("pedido");
    const totalElement = document.getElementById("total");

    // Inicializar el total del pedido
    let total = 0;

    // Inicializar la tabla de pedido en el HTML
    pedido.innerHTML = `
        <tr>
            <th>Cantidad</th>
            <th>Nombre</th>
            <th>Precio Unitario</th>
            <th>Precio Total</th>
        </tr>
    `;

    // Función para agregar un elemento al pedido y actualizar el total
    function agregarAlPedido(item, precio, cantidad) {
        const row = document.createElement("tr");
        const precioTotal = cantidad * precio;

        // Agregar la información del producto al pedido
        row.innerHTML = `
            <td>${cantidad}</td>
            <td>${item}</td>
            <td>${precio} COP</td>
            <td>${precioTotal} COP</td>
        `;

        pedido.appendChild(row);
        total += precioTotal;
    }

    // Agregar plato seleccionado al pedido si está definido
    if (platoSeleccionado) {
        const precioPlato = precios[platoSeleccionado];
        agregarAlPedido(platoSeleccionado, precioPlato, cantidadPlatos);
    }

    // Agregar bebida seleccionada al pedido si está definida
    if (bebidaSeleccionada) {
        const precioBebida = precios[bebidaSeleccionada];
        agregarAlPedido(bebidaSeleccionada, precioBebida, cantidadBebidas);
    }

    // Agregar plato ejecutivo al pedido si está marcado
    if (platoEjecutivo) {
        const precioPlatoEjecutivo = precios.platoEjecutivo;
        agregarAlPedido("Plato Ejecutivo", precioPlatoEjecutivo, 1);
        total += precioPlatoEjecutivo;
    }

    // Mostrar el total del pedido en la página
    totalElement.textContent = total + " COP";

    // Mostrar el apartado de pedido en la página
    pedido.style.display = "table";
}
