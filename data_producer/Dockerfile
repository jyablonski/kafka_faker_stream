FROM python:3.8-slim as base

COPY data_producer/requirements.txt ./requirements.txt

RUN apt-get update &&\
    apt-get -y upgrade &&\
    apt-get -y install --no-install-recommends git &&\
    apt-get -y install --no-install-recommends gcc &&\
    pip install --upgrade pip

RUN pip install -r requirements.txt

COPY data_producer/app.py ./app.py
COPY data_producer/example.log ./example.log

CMD ["python3", "app.py"]
