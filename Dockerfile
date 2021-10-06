FROM python:3.9.6

WORKDIR /interpolacao-de-newton-python

COPY requirements.txt  requirements.txt
COPY shell-scripts/command.sh command.sh

RUN pip install -r requirements.txt
