# https://github.com/kataev/pytest-grpc/blob/master/example/test_example.py


import grpc
import threading
from toxic_server.grpc_server import serve
from toxic_server import inference_pb2, inference_pb2_grpc

server_thread = threading.Thread(target=serve, daemon=True)
server_thread.start()


def test_grpc_toxic():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = inference_pb2_grpc.TextClassifierStub(channel)
        response = stub.Predict(
            inference_pb2.TextClassificationInput(text="Listen here you dumbass")
        )
        assert response.is_toxic


def test_grpc_non_toxic():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = inference_pb2_grpc.TextClassifierStub(channel)
        response = stub.Predict(
            inference_pb2.TextClassificationInput(
                text="Thank you, have a pleasant evening"
            )
        )
        assert not response.is_toxic
