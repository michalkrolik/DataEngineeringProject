FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev vim cron\
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && pip3 install forex_python pymongo pandas_datareader azure-storage-blob

WORKDIR /app
COPY ./main.py /app
COPY ./exporter.py /app
COPY ./starter.sh /app
COPY ./hello-cron /etc/cron.d/hello-cron

RUN chmod 0644 /etc/cron.d/hello-cron

RUN crontab /etc/cron.d/hello-cron
RUN chmod u+x /app/starter.sh
RUN chmod u+x /app/main.py
RUN chmod u+x /app/exporter.py

RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log
