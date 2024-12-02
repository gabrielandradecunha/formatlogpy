FROM ubuntu:latest

RUN apt-get update && apt-get install python3 -y

RUN mkdir /app

RUN chmod -R 777 app/

COPY . /app

WORKDIR /app