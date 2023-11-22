// Variables para almacenar la cantidad y precios de los libros
let cantidadJava = 0;
let cantidadCSharp = 0;
let precioJava = 10; // Precio ficticio para el libro de Java
let precioCSharp = 15; // Precio ficticio para el libro de C#

// Función para aumentar la cantidad de un libro
function aumentarCantidad(libro) {
    if (libro === 'java') {
        cantidadJava++;
        actualizarCantidad('java', cantidadJava);
        actualizarTabla();
    } else if (libro === 'csharp') {
        cantidadCSharp++;
        actualizarCantidad('csharp', cantidadCSharp);
        actualizarTabla();
    }
}

// Función para disminuir la cantidad de un libro
function disminuirCantidad(libro) {
    if (libro === 'java' && cantidadJava > 0) {
        cantidadJava--;
        actualizarCantidad('java', cantidadJava);
        actualizarTabla();
    } else if (libro === 'csharp' && cantidadCSharp > 0) {
        cantidadCSharp--;
        actualizarCantidad('csharp', cantidadCSharp);
        actualizarTabla();
    }
}

// Función para actualizar la cantidad visualmente en la página
function actualizarCantidad(libro, cantidad) {
    document.getElementById(libro + 'Cantidad').innerText = cantidad;
}

// Función para actualizar la tabla de libros y el valor total
function actualizarTabla() {
    const tabla = document.getElementById('tablaLibros');
    const tbody = tabla.getElementsByTagName('tbody')[0];

    // Limpiar la tabla antes de actualizar
    tbody.innerHTML = '';

    // Actualizar la tabla con los libros y precios
    if (cantidadJava > 0) {
        agregarFilaTabla('java', 'Libro de Java', precioJava, cantidadJava);
    }
    if (cantidadCSharp > 0) {
        agregarFilaTabla('csharp', 'Libro de C#', precioCSharp, cantidadCSharp);
    }

    // Actualizar el valor total
    actualizarValorTotal();
}

// Función para agregar una fila a la tabla con la información del libro
function agregarFilaTabla(libro, nombre, precioUnitario, cantidad) {
    const tabla = document.getElementById('tablaLibros');
    const tbody = tabla.getElementsByTagName('tbody')[0];

    const precioTotal = precioUnitario * cantidad;

    const fila = document.createElement('tr');
    fila.innerHTML = `<td>${cantidad}</td>
                        <td>${nombre}</td>
                        <td>$${precioUnitario}</td>
                        <td>$${precioTotal}</td>`;

    tbody.appendChild(fila);
}

// Función para actualizar el valor total de la compra
function actualizarValorTotal() {
    const totalJava = precioJava * cantidadJava;
    const totalCSharp = precioCSharp * cantidadCSharp;
    const valorTotal = totalJava + totalCSharp;

    document.getElementById('total').innerText = valorTotal;
}
