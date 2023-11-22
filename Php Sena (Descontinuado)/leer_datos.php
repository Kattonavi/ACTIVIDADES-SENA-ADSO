<?php
$conexion = new mysqli('localhost', 'root', '','pruebadatos');
if ($conexion->connect_errno){
    die ('lo siento hubo un problemaen la conexion');
}else{
    $slq = "SELECT * FROM usuarios";
    $resultado = $conexion->query($slq);

    if ($resultado->num_rows){
        while($fila = $resultado->fetch_assoc()){

            echo $fila ['ID'].' '. $fila ['nombre']. '<br/>';
        }
    }else{
        echo 'no hay datos';
    }
}
?>
