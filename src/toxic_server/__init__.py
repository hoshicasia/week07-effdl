import sys

from . import inference_pb2 as _inference_pb2

sys.modules.setdefault("inference_pb2", _inference_pb2)
