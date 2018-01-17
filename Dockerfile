FROM python:alpine
MAINTAINER "wojciech@smolak.pl"
COPY . /coin-calc-app
WORKDIR /coin-calc-app
RUN pip install -r requirements.txt
RUN mkdir logs && echo "Let's get it started!" > logs/logfile
RUN cp run.sh /etc/periodic/15min/run && chmod a+x /etc/periodic/15min/run
CMD crond && tail -f logs/logfile