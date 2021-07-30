from concurrent import futures
import logging
import grpc
from chat import test_pb2, test_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = test_pb2_grpc.ChatServiceStub(channel)

message = stub.SendMessage(test_pb2.Message(body="Hey, How're you doing?"))

print(message.body)