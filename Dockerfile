FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /src/

RUN apt-get update && \
    apt-get install -y python3-pip

COPY requirements.txt /src/

RUN pip install -r /src/requirements.txt

COPY . .
