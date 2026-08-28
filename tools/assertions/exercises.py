from tools.assertions.base import assert_equal
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema, \
    ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesResponseSchema
from clients.errors_schema import InternalErrorResponseSchema
from tools.assertions.errors import assert_internal_error_response
from tools.assertions.base import assert_length
import allure
from tools.logger import get_logger

logger = get_logger("EXERCISES_ASSERTIONS")


@allure.step("Check create exercise response")
def assert_create_exercise_response(actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema):
    """
    Сравнение данных запроса на создание упражнения и данных ответа

    :param actual: Данные ответа запроса на создание упражнения
    :param expected: Данные запроса на создание упражнения
    :return: None
    """
    logger.info("Check create exercise response")

    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.exercise.course_id, expected.course_id, "course_id")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")


@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Сверяет данные упражнения, ожидаемые и полученные

    :param actual: Фактические данные упражнения
    :param expected: Ожидаемые данные упражнения
    :return: None
    """
    logger.info("Check exercise")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Check get exercise response")
def assert_get_exercise_response(actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema):
    """
    Сверяет данные ответа на запрос упражнения и ответа на создание упражнения

    :param actual: Ответ на запрос упражнения
    :param expected: Ответ на создание упражнения
    :return: None
    """
    logger.info("Check get exercise response")

    assert_exercise(actual=actual.exercise, expected=expected.exercise)


@allure.step("Check update exercise response")
def assert_update_exercise_response(actual: UpdateExerciseResponseSchema, expected: UpdateExerciseRequestSchema):
    """
    Сверяет данные запроса и данные ответа обновления упражнения

    :param actual: Данные ответа на обновление упражнения
    :param expected: Данные запроса на обновление упражнения
    :return: None
    """
    logger.info("Check update exercise response")

    if expected.title is not None:
        assert_equal(actual.exercise.title, expected.title, "title")
    if expected.min_score is not None:
        assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    if expected.max_score is not None:
        assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    if expected.order_index is not None:
        assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    if expected.description is not None:
        assert_equal(actual.exercise.description, expected.description, "description")
    if expected.estimated_time is not None:
        assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если задание не найдено на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    logger.info("Check exercise not found response")

    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)


@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка заданий соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка заданий.
    :param create_exercise_responses: Список API ответов при создании заданий.
    :raises AssertionError: Если данные заданий не совпадают.
    """
    logger.info("Check get exercises response")

    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)
