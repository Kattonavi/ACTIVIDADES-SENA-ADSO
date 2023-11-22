function Sumar(n1,n2){
    var resultado=n1+n2;
    var res=document.getElementById("resultado")
    if(n1!=0 && n2!=0){
        respuesta.style.display="block";
        res.innerHTML = `Total : ${resultado};`
        res.style.color="green";
    }else{
        respuesta.style.display="block";
        res.innerHTML = `verifique sus datos`;
        res.style.color="red";
    }
}
function Restar(){
    let n1=parseInt(document.getElementById("n1").value)
    let n2=parseInt(document.getElementById("n2").value)
    resultado=n1-n2;
    document.write("el valor de la resta es "+resultado)
}
function Multiplicar(){
    let n1=parseInt(document.getElementById("n1").value)
    let n2=parseInt(document.getElementById("n2").value)
    resultado=n1n2;
    document.write("el valor de la multiplicacion es "+resultado)
}
function Dividir(){
    let n1=parseInt(document.getElementById("n1").value)
    let n2=parseInt(document.getElementById("n2").value)
    resultado=n1/n2;
    document.write("el valor de la division es "+resultado)
}
function Potencia(){
    let n1=parseInt(document.getElementById("n1").value)
    resultado=n1n1;
    document.write("el valor de la potencia es "+resultado)
}

function mostrar(){
    let n1=parseInt(document.getElementById("n1").value)
    let n2=parseInt(document.getElementById("n2").value)
    let opc=parseInt(document.getElementById("opc").value)
    switch(opc){
        case 1:
            Sumar(n1,n2)
            break;
        case 2:
            Restar()
            break;
        case 3:
            Multiplicar()
            break;
        case 4:
            Dividir()
            break;
        case 5:
            Potencia()
            break;
        case 6:
            mostrar()
            break;


    }
}