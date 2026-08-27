import grpc
from concurrent import futures

import course_service_pb2
import course_service_pb2_grpc

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):

    def GetCourse(self, request, context):
        print(f'Получен запрос курса: {request.course_id}')
        return course_service_pb2.GetCourseResponse(course_id = request.course_id, title = 'Автотесты API', description = 'Будем изучать написание API автотестов')

def serve():
    #количество потоков
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    #регистрация обработчика
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    #Проброс портов
    server.add_insecure_port("[::]:50051")

    #Запуск сервера
    server.start()
    print("Сервер запущен на порту 50051")

    #Отключение сервера
    server.wait_for_termination()


if __name__ == '__main__':
    serve()