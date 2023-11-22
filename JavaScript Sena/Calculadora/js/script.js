// Función para sumar dos números y mostrar el resultado en un elemento HTML
function Sumar(n1, n2) {
    var resultado = n1 + n2;
    var res = document.getElementById("resultado");

    // Verifica que ambos números sean diferentes de cero antes de mostrar el resultado
    if (n1 != 0 && n2 != 0) {
        // Muestra el resultado en un elemento con id 'resultado'
        respuesta.style.display = "block";
        res.innerHTML = `Total: ${resultado}`;
        res.style.color = "green";
    } else {
        // Muestra un mensaje de verificación si alguno de los números es cero
        respuesta.style.display = "block";
        res.innerHTML = `Verifique sus datos`;
        res.style.color = "red";
    }
}

// Función para restar dos números y mostrar el resultado en una ventana emergente
function Restar() {
    // Obtiene los valores de los números desde elementos con id 'n1' y 'n2'
    let n1 = parseInt(document.getElementById("n1").value);
    let n2 = parseInt(document.getElementById("n2").value);
    
    // Realiza la resta y muestra el resultado en una ventana emergente
    resultado = n1 - n2;
    document.write("El valor de la resta es " + resultado);
}

// Función para multiplicar dos números y mostrar el resultado en una ventana emergente
function Multiplicar() {
    // Obtiene los valores de los números desde elementos con id 'n1' y 'n2'
    let n1 = parseInt(document.getElementById("n1").value);
    let n2 = parseInt(document.getElementById("n2").value);
    
    // Realiza la multiplicación y muestra el resultado en una ventana emergente
    resultado = n1 * n2;
    document.write("El valor de la multiplicación es " + resultado);
}

// Función para dividir dos números y mostrar el resultado en una ventana emergente
function Dividir() {
    // Obtiene los valores de los números desde elementos con id 'n1' y 'n2'
    let n1 = parseInt(document.getElementById("n1").value);
    let n2 = parseInt(document.getElementById("n2").value);
    
    // Realiza la división y muestra el resultado en una ventana emergente
    resultado = n1 / n2;
    document.write("El valor de la división es " + resultado);
}

// Función para elevar un número a la potencia y mostrar el resultado en una ventana emergente
function Potencia() {
    // Obtiene el valor del número desde un elemento con id 'n1'
    let n1 = parseInt(document.getElementById("n1").value);
    
    // Eleva al cuadrado y muestra el resultado en una ventana emergente
    resultado = n1 ** 2; // Elevar al cuadrado, ya que parece ser una potencia de 2
    document.write("El valor de la potencia es " + resultado);
}

// Función principal que determina la operación a realizar según la opción seleccionada
function mostrar() {
    // Obtiene los valores de los números y la opción desde elementos HTML
    let n1 = parseInt(document.getElementById("n1").value);
    let n2 = parseInt(document.getElementById("n2").value);
    let opc = parseInt(document.getElementById("opc").value);

    // Realiza la operación correspondiente según la opción seleccionada
    switch (opc) {
        case 1:
            Sumar(n1, n2);
            break;
        case 2:
            Restar();
            break;
        case 3:
            Multiplicar();
            break;
        case 4:
            Dividir();
            break;
        case 5:
            Potencia();
            break;
        case 6:
            mostrar(); 
            break;
    }
}
