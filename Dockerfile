FROM alpine:latest

RUN apk add --update --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python

RUN pip install python-dotenv pyarr

RUN mkdir -p /opt/scripts/radarr_autodelete

COPY radarr_autodelete.py /opt/scripts/radarr_autodelete

RUN touch /etc/periodic/radarr_autodelete

RUN echo "0 3 * * * python3 /opt/scripts/radarr_autodelete/radarr_autodelete.py --keeptime $KEEPTIME --filtertag $FILTERTAG --verbose" >> /etc/periodic/radarr_autodelete

RUN chmod 0644 /etc/periodic/radarr_autodelete

RUN crontab /etc/periodic/radarr_autodelete

RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log