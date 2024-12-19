#!/bin/bash

uvicorn service_file_to_text.lambdas.handler:app --host 0.0.0.0 --port 8080