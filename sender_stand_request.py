import configuration
import requests
import data             #Este archivo almacenará la información que se enviará en la solicitud, como el cuerpo y los encabezados

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)
#----


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print (response.status_code)
#---

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,             # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
#---

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())
#---

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)

response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.json())
#---

def get_new_user_token():
    response = post_new_user((data.user_body))
    response_json = response.json()
    return response_json["authToken"]


#---

def post_new_client_kit(kit_body):
    auth_token = get_new_user_token()
    authorization = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer "{auth_token}'
    }
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=authorization
                         )

    response = _new_user_token(authorization)
    print(response.status_code)
    print(response.json())

#---
