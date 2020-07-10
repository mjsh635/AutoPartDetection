"""The Python implementation of the GRPC helloworld. Greeter server."""

from concurrent import futures
import logging
import AutoPartDetect_pb2_grpc
import AutoPartDetect_pb2
import json

import grpc

mydict = {"ID": 1225,"AGE":23}

class AutoPartDetection(AutoPartDetect_pb2_grpc.AutoPartDetection):

    def Get_List_of_Tags(self, request, context):
        print(request)
        resp = AutoPartDetect_pb2.Get_List_of_Tags_Response()
        return resp
    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    AutoPartDetect_pb2_grpc.add_AutoPartDetectionServicer_to_server(AutoPartDetection(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    while True:

        serve()