FROM python:3.12-slim

RUN pip install mangum uvicorn httpx fastapi
RUN pip install osbot-aws osbot-fast-api
RUN pip install cbr_custom_open_sec_summit

RUN pip install markitdown
RUN pip install python-multipart

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install pytesseract pillow


COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.4 /lambda-adapter /opt/extensions/lambda-adapter

RUN python --version
ENV PORT=8080

WORKDIR /app
COPY ../../../cbr_custom_open_sec_summit /app/cbr_custom_open_sec_summit

ENV PYTHONPATH="/app"

COPY ./deploy/docker/cbr_custom/start.sh /app/start.sh

CMD ["./start.sh"]

