from concurrent import futures
import os
import grpc
from toxic_server import inference_pb2, inference_pb2_grpc
from toxic_server.model import predict


class TextClassifierServicer(inference_pb2_grpc.TextClassifierServicer):
    def Predict(self, request, context):
        return inference_pb2.TextClassificationOutput(is_toxic=predict(request.text))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inference_pb2_grpc.add_TextClassifierServicer_to_server(
        TextClassifierServicer(), server
    )
    port = int(os.environ.get("GRPC_PORT", "50051"))
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
