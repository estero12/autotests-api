from httpx import Response
import allure
from clients.api_client import APIClient
from clients.exercises.exercises_schema import (GetExercisesRequestSchema, CreateExerciseRequestSchema,
                                                UpdateExerciseRequestSchema, CreateExerciseResponseSchema,
                                                GetExerciseResponseSchema, GetExercisesResponseSchema,
                                                UpdateExerciseResponseSchema)
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    """
    Клиент взаимодействия с /api/v1/exercises.
    """

    @allure.step("Get exercises")
    def get_exercises_api(self, request: GetExercisesRequestSchema) -> Response:
        """
        Получение списка упражнений курса

        :param request: Словарь с параметрами запроса упражнений курса см.GetExercisesRequestSchema
        :return: Ответ в формате httpx.Response
        """
        return self.get(f'{APIRoutes.EXERCISES}',
                        params=request.model_dump(by_alias=True))

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение упражнения по id

        :param exercise_id: id упражнения
        :return: Ответ в формате httpx.Response
        """
        return self.get(f'{APIRoutes.EXERCISES}/{exercise_id}')

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Создание упражнения

        :param request: Словарь со структурой упражнения см.CreateExerciseQueryDict
        :return: Ответ в формате httpx.Response
        """
        return self.post(f'{APIRoutes.EXERCISES}', json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Обновление упражнения

        :param exercise_id: id упражнения
        :param request: Словарь с обновляемыми полями упражнения см.UpdateExerciseQueryDict
        :return: Ответ в формате httpx.Response
        """
        return self.patch(f'{APIRoutes.EXERCISES}/{exercise_id}', json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление упражнения

        :param exercise_id: id упражнения
        :return: Ответ в формате httpx.Response
        """
        return self.delete(f'{APIRoutes.EXERCISES}/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, request: GetExercisesRequestSchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(request)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id=exercise_id, request=request.model_dump(by_alias=True))
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Возвращает настроенный клиент ExercisesClient

    :param user: данные для авторизации пользователя см.AuthenticationUserDict
    :return: клиент ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))
