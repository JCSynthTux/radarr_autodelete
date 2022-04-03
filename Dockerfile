FROM python:latest

#RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

RUN pip install python-dotenv pyarr

RUN mkdir -p /opt/scripts/radarr_autodelete

COPY radarr_autodelete.py /opt/scripts/radarr_autodelete

RUN touch /etc/cron.d/radarr_autodelete

RUN echo "* * * * * python3 /opt/scripts/radarr_autodelete/radarr_autodelete.py --keeptime $KEEPTIME --filtertag $FILTERTAG --verbose" >> /etc/cron.d/radarr_autodelete

RUN chmod 0644 /etc/cron.d/radarr_autodelete

RUN crontab /etc/cron.d/radarr_autodelete

RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log