FROM python:3.11

WORKDIR /effdl26-week07-homework

RUN pip install supervisor
RUN pip install uv

COPY pyproject.toml .
COPY src ./src
COPY proto ./proto
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN uv pip install --system .

RUN python -m grpc_tools.protoc \
    -I proto \
    --python_out=src/toxic_server \
    --grpc_python_out=src/toxic_server \
    proto/inference.proto

ENV HF_HOME=/model_cache
RUN python -c "from transformers import pipeline; pipeline('text-classification', model='unitary/toxic-bert')"

ENV PYTHONPATH=/effdl26-week07-homework/src/toxic_server

EXPOSE 5000
EXPOSE 50051

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]