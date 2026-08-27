import grpc;

import course_service_pb2
import course_service_pb2_grpc

#Создание канала связи и клиента
channel = grpc.insecure_channel("localhost:50051")
stub = course_service_pb2_grpc.CourseServiceStub(channel)

#Отправка запроса к серверу
response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course"))
print(f'Идентификатор курса: {response.course_id}\n'
      f'Наименование курса: {response.title}\n'
      f'Описание курса: {response.description}\n')