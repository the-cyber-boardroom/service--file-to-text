#!/bin/bash

uvicorn cbr_custom_open_sec_summit.lambdas.handler:app --host 0.0.0.0 --port 8080