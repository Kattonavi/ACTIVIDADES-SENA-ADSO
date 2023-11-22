nacimiento=parseInt(prompt("ingrese tu año de nacimiento"))
console.log(typeof(nacimiento));
const fecha = new Date();
const fechaActual=fecha.getFullYear();
let edad=fechaActual-nacimiento;


var nombre=prompt("Ingrese tu nombre");
//var edadn=parseInt(prompt("ingresa la edad"))



if(edad<=8){
    document.write("Bienvenido mi criado " +nombre+" me alegra saber que su edad es "+edad+" años, pero lamento decrile que no puede pasar")}
else if(edad<=17){
    document.write("Bienvenido mi joven " +nombre+" me alegra saber que su edad es "+edad+" años, pero lamento decirle que es menor de edad y no puede pasar")
}else{
    document.write("Bienvenido mi estimado " +nombre+" me alegra saber que su edad es "+edad+" años, eres mayor de edad, puedes pasar sin ningun problema")
}




