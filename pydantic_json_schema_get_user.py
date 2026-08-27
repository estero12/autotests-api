from httpcore import _api

from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

# Создание пользователя
create_user_response = public_users_client.create_user(create_user_request)

auth_user_request = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(auth_user_request)
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# Получение пользователя
get_user_response = private_users_client.get_user_api(create_user_response.user.id)
validate_json_schema(instance=get_user_response.json(),schema=get_user_response_schema)