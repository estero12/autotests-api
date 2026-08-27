import httpx

login_payload = {
    "email": "user@example.com",
    "password": "1"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
access_token = f"Bearer {login_response_data["token"]["accessToken"]}"
refresh_token = login_response_data["token"]["refreshToken"]

print("Status code: ", login_response.status_code)
print(f"ACCESS TOKEN: {access_token}")
print(f"REFRESH TOKEN: {refresh_token}")

me_headers = {
    "Authorization": access_token
}

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=me_headers)
me_response_json = me_response.json()

print("Status code: ", me_response.status_code)
print("Me data: ", me_response_json)
