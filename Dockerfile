FROM pytorch/pytorch:2.11.0-cuda12.8-cudnn9-runtime

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

RUN pip install --no-cache-dir "runpod>=1.7.0"

COPY handler.py /app/handler.py

CMD ["python", "-u", "/app/handler.py"]