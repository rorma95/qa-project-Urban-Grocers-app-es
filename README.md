# Pruebas para el parámetro firstName al crear un/a usuario/a en []
## _Proyecto final de Sprint No. 7 "Introducción a la automatización de pruebas"_

## Tarea:
    Otro QA Engineer que trabaja contigo está comprobando cómo la aplicación Urban Grocers crea kits de productos. 
    Se han creado varias listas de comprobación, una de ellas es para el campo name en la solicitud de creación 
    de un kit de productos. 
    La tarea es automatizar las pruebas desde esta lista de comprobación, cargar el código en GitHub y enviar el 
    repositorio a revisión.

## Requisitos
- Solo se probara la logica de la funcion de agregar nombre a un kit nuevo.
- Se haran pruebas negativas y positivas.
- Se deberan probar el ingreso de numeros como string y enteros.
- No se permitira lineas de codigo comentadas si no son informativas.
- Se entregara el codigo escrito en python.

## Se necesitaran seis archivos en total:
- Configuration.py, 
- data.py, 
- sender_stand_request.py, 
- create_kit_name_kit_test.py, 
- README.md. 
- .gitignore. 

## Pasos a seguir, usando pycharm:
- Obtener un servidor para la aplicacion Urban Grocers.
- Crear una funcion para creea un nuevo usuario.
- Guardar el nuevo usuario en el codigo para poder crear un nuevo kit
- Probar los requisitos para el campo name del kit "crea tu propio kit"

## Contenido de los diferentes archivos
- Configuration.py: Aqui se guardo, en variables, las rutas que se deben de seguir, en la api, para realizar las diferentes acciones en la aplicacion Urban Grocers. Ademas de que se guardo tambien el link del servidor que se uso.
- data.py: Se guarda en diccionarios la informacion requerida que se vas a utilizar para posteriormente ser editada y usada en las pruebas.
- sender_stand_request.py: Se guardan funciones, por ejemplo, para crear y obtener nuevos usuarios y kits,  
- create_kit_name_kit_test.py: Archivo principal donde declaran funciones para las pruebas positivas y negativas ademas de las pruebas en si mismas. 
- README.md: Breve descripción de tu proyecto
- .gitignore: Archivo especial para que no se suban en los repositorios archivos inecesarios o por temas de seguridad se deban de ignorar.

## Pruebas realizadas.
-	El número permitido de caracteres (1): Limite menor
- 	El número permitido de caracteres (511): Limite mayor
-   El número de caracteres es menor que la cantidad permitida (0): Menos caracteres de los permitidos
- 	El número de caracteres es mayor que la cantidad permitida (512): Mas caracteres que los permitdos
- 	Se permiten caracteres especiales: Caracteres permitidos
-   Se permiten espacios: Nombre con espacios
- 	Se permiten números: Nombre con string de numeros
-   El parámetro no se pasa en la solicitud: Campo name vacio.
- 	Se ha pasado un tipo de parámetro diferente (número): Se ingreso numero entero, diferente tipo de dato.
