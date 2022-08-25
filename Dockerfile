FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y cron python3 python3-pip

RUN pip install python-dotenv pyarr

RUN mkdir -p /opt/scripts/radarr_autodelete

COPY radarr_autodelete.py /opt/scripts/radarr_autodelete

COPY radarr-autodelete-cron /etc/cron.d/radarr-autodelete-cron

RUN chmod 0644 /etc/cron.d/radarr-autodelete-cron

RUN crontab /etc/cron.d/radarr-autodelete-cron

RUN touch /var/log/cron.log

CMD cron -f -l 2 && tail -f /var/log/cron.log
