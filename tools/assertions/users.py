import allure

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema
from tools.assertions.base import assert_equal
from tools.logger import get_logger  # Импортируем функцию для создания логгера

logger = get_logger("USERS_ASSERTIONS")  # Создаем логгер с именем "USERS_ASSERTIONS"

@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create user response")

    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")

@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверка соответствия данных пользователя

    :param actual: Данные пользователя
    :param expected: Ожидаемые данные пользователя
    :return: None
    """
    # Логируем факт начала проверки
    logger.info("Check user")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")

@allure.step("Check get user response")
def assert_get_user_response(get_user_response:GetUserResponseSchema,create_user_response: CreateUserResponseSchema):
    """
    Проверка соответствия данных при создании и получении пользователя

    :param get_user_response: Ответ на запрос пользователя
    :param create_user_response: Ответ на создание пользователя
    :return: None
    """
    # Логируем факт начала проверки
    logger.info("Check get user response")

    assert_equal(get_user_response.user.id, create_user_response.user.id, "id")
    assert_equal(get_user_response.user.email, create_user_response.user.email, "email")
    assert_equal(get_user_response.user.first_name, create_user_response.user.first_name, "first_name")
    assert_equal(get_user_response.user.middle_name, create_user_response.user.middle_name, "middle_name")
    assert_equal(get_user_response.user.last_name, create_user_response.user.last_name, "last_name")
