FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /code

ADD . /code
RUN python -m pip install -r requirements.txt
