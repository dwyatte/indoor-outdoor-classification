#!/bin/sh

docker-compose up tensorflow-serving & \
sleep 5
export TF_SERVING_URL=localhost:8500 && python classification/run.py $@ && \
docker-compose down -v
