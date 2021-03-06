FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /code

ADD requirements.txt /code
ADD bin/docker-entrypoint.sh /code/bin
RUN python -m pip install -r requirements.txt

ENTRYPOINT [ "./bin/docker-entrypoint.sh" ]