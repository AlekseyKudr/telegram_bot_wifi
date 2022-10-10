FROM python:3.8

RUN mkdir /tggdz
COPY *.py /tggdz
WORKDIR /tggdz

RUN apt-get update && apt-get upgrade && pip install --upgrade pip && pip install pyTelegramBotAPI

ENTRYPOINT ["python", "server.py"]
