<?php
$conexion = new mysqli('localhost', 'root','','pruebadatos' );
if ($conexion ->connect_errno){
    die('lo siento hubo un problema en la conexion');
    }else{
        $sql = "INSERT INTO usuarios(ID, nombre, edad) VALUES(null,'maria P', 30)";
        $resultado = $conexion->query($sql);
        if($conexion->affected_rows >=1){
            echo 'Filas agregadas: ' . $conexion->affected_rows;
        }
    
    }


?>