from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import AuthenticationUserSchema
from clients.users.users_schema import CreateUserRequestSchema
from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from config import settings

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()

# Создание пользователя
create_user_response = public_users_client.create_user(create_user_request)
print("Созданный пользователь: ", create_user_response)

# Данные для авторизации
auth_request = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Создание приватных клиентов
files_client = get_files_client(auth_request)
course_client = get_courses_client(auth_request)
exercise_client = get_exercise_client(auth_request)

# Загрузка файла
create_file_request = CreateFileRequestSchema(upload_file=settings.test_data.image_png_file)
create_file_response = files_client.create_file(create_file_request)
print("Созданный файл: ", create_file_response)

# Создание курса
create_course_request = CreateCourseRequestSchema(
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = course_client.create_course(create_course_request)
print("Созданный курс: ", create_course_response)

# Создание упражнения
create_exercise_request = CreateExerciseRequestSchema(
    courseId=create_course_response.course.id
)

create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print("Данные созданного упражнения: ", create_exercise_response)
