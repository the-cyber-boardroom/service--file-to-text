FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install mangum uvicorn httpx fastapi python-multipart
RUN pip install osbot-aws osbot-fast-api
RUN pip install markitdown pytesseract pillow

RUN pip install service_file_to_text



COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.4 /lambda-adapter /opt/extensions/lambda-adapter

RUN python --version
ENV PORT=8080

WORKDIR /app
COPY ../../../service_file_to_text /app/service_file_to_text

ENV PYTHONPATH="/app"

COPY ./deploy/docker/service/start.sh /app/start.sh

CMD ["./start.sh"]

