from concurrent import futures
import logging
import grpc
from chat import test_pb2, test_pb2_grpc

class ChatServer(test_pb2_grpc.ChatServiceServicer):

    def SendMessage(self, request, context):
        message = request.body

        print("Message Received!", message)

        return test_pb2.Message(body="ACK! Message Received.")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=50))
    test_pb2_grpc.add_ChatServiceServicer_to_server(
        ChatServer(), server
    )
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()