import httpx

from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data =create_user_response.json()

print("Create user status code:", create_user_response.status_code)
print("Create user data:", create_user_response_data)

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
access_token = login_response_data["token"]["accessToken"]

print("Login status code:",login_response)
print("Login response data:", login_response_data)

auth_headers = {
    "Authorization":f"Bearer {access_token}"
}

update_payload = {
  "email":  email(),
  "lastName": "Конохов",
  "firstName": "Артур",
  "middleName": "Валентинович"
}

update_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}",json=update_payload, headers=auth_headers)
update_response_data = update_response.json()

print("Update status code:",update_response.status_code)
print("Update response data:", update_response_data)

