FROM ubuntu:latest

WORKDIR /app
COPY ./main.py /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev vim cron\
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && pip3 install forex_python pymongo \
  && crontab -l > mycron \
  && echo "0 * * * * python3 /app/main.py" > mycron \
  && crontab mycron && rm mycron