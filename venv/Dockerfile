# start by pulling the python image
FROM python:slim-buster


WORKDIR /usr/src/app

ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y default-libmysqlclient-dev libssl-dev tk && \
    apt-get install -y --no-install-recommends gcc python-dev

RUN /usr/local/bin/python -m pip install --upgrade pip
# COPY requirements.txt ./

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p /root/.ssh/

USER root

RUN /usr/sbin/groupadd -g 1000 user && /usr/sbin/useradd -g 1000 -r user

RUN chmod 777 ./app/attendance_processer/attendance_csv_files

ENV FLASK_APP=app/app.py

USER user

VOLUME /app

ENTRYPOINT [ "flask" ]

CMD [ "run" ]

# CMD ["flask", "run", "--host=0.0.0.0"]

# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "{.venv}.{app}:webapp"]

