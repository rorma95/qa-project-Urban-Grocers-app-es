import sender_stand_request
import data

#Preparacion de las  pruebas, declarar funciones positivas y negativas


def get_kit_body(name_nkb):                                         #Esta funcion cambia los valores del parametro 'name' del kit_body en data
    kit_body = data.kit_body.copy()                                 #El dic que contiene el cuerpo de la solicitud se copia del archivo 'data'  para conservar los datos del dic de origen

    kit_body["name"] = name_nkb                                     #Se devuelve un nuevo diccionario con el valor firstName requerido
    return kit_body

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def positve_assert_conjunto_primavera(name_nkb):
    kit_body = get_kit_body(name_nkb)                               #El cuerpo de la soliocitud actualizada se guarda en la variable kit_body
    response = sender_stand_request.post_new_client_kit(kit_body)
                                                                    #Envia la solicitud para crear un nuevo kit con el token del usuario creado usuario se guarda en la variable response

    assert response.status_code ==201                               #Comprueba si el codigo de estado es 201

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def negative_assert_conjunto_primavera(name_nkb):
    kit_body = get_kit_body(name_nkb)                               # utiliza el nombre proporcionado para obtener el cuerpo del kit
    kit_negative_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_negative_response.status_code ==400                  #Verifica que la solicitud no se ha realizado con exito
    assert kit_negative_response.json()["code"] == 400              # Comprueba si el codigo de error en la respuesta es 400
    assert kit_negative_response.json()["message"] == "kit name's is empty"

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def negative_assert_no_name_conjunto_primavera(name_nkb):           # La respuesta contiene el siguiente mensaje de error: "No se han enviado todos los parámetros requeridos"
    kit_body = get_kit_body(name_nkb)
    response = sender_stand_request.post_new_client_kit(kit_body)   # La variable "response" almacena el resultado de la solicitud user_body.
    assert response.status_code == 400                              # Comprueba si la respuesta contiene el código 400

    assert response.json()["code"] == 400                           # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["message"] == "No se enviaron todos los parámetros necesarios"
                                                                    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Prueba 1. Creación de un nuevo kit con cantidad de caracteres permitidos
# El numero permitido de caracteres (1): kit_body = {"name": "a"}
def test_kit_body_name_1_character_name_get_success_response():     # La versión actualizada del cuerpo de solicitud para un  nuevo kit con el nombre "a" se guarda en la variable "user_body"
    positve_assert_conjunto_primavera("a")                          #kit_body = {"name_nkb": "a"}

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Prueba 2. Creación de un nuevo nuevo kit con cantidad maxima de caracteres permitidos
#El número maximo permitido de caracteres (511)
def test_kit_body_name_511_character_name_get_success_response():
    positve_assert_conjunto_primavera("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Prueba 3. Creación de un nuevo nuevo kit con cantidad menor de caracteres permitidos
#El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
def test_kit_body_name_0_character_name_get_success_response():
    negative_assert_conjunto_primavera("")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Prueba 4. Creación de un nuevo nuevo kit con cantidad mayor de caracteres permitidos
#El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
def test_kit_body_name_512_character_name_get_success_response():
    negative_assert_conjunto_primavera("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Prueba 5. Creación de un nuevo nuevo kit con caracteres especiales
#Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
def test_kit_body_name_special_character_name_get_success_response():
    positve_assert_conjunto_primavera("$#@")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Prueba 6. Creación de un nuevo nuevo kit con nombre con espacio
#Se permiten espacios: kit_body = { "name": " A Aaa " }
def test_kit_body_name_space_character_name_get_success_response():
    positve_assert_conjunto_primavera(" A Aaa ")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Prueba 7. Creación de un nuevo nuevo kit con nombre de strinng de numeros
#Se permiten números: kit_body = { "name": "123" }
def test_kit_body_name_number_character_no_name_get_success_response():
    positve_assert_conjunto_primavera("123")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Prueba 8. Creación de un nuevo nuevo kit con nombre sin llenar
#	El parámetro no se pasa en la solicitud: kit_body = { }
def test_kit_body_name_No_name_get_success_response():
    kit_body = data.kit_body.copy()

    kit_body.pop("name")
    negative_assert_no_name_conjunto_primavera(kit_body)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#No.9
#Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
def test_kit_body_name_different_character_name_get_success_response():
    negative_assert_conjunto_primavera(123)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
