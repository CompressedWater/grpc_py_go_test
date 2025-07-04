import logging

import grpc
from proto import py_go_basic_pb2
from proto import py_go_basic_pb2_grpc


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = py_go_basic_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(py_go_basic_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()