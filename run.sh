#!/bin/bash

docker build . -t lsc_host
docker run -p 8501:8501 -d lsc_host