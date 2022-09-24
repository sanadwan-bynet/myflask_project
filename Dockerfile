# start by pulling the python image
FROM python:alpine

EXPOSE 5000

WORKDIR /app

# ENV PYTHONBUFFERED 1

# ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

RUN apt update

# RUN apt-get -y install build-essential
RUN /usr/local/bin/python -m pip install --upgrade pip

# RUN pip install markupsafe==1.1.1 flask
RUN /usr/sbin/addgroup -g 1000 sanad && /usr/sbin/adduser -u 1000 -g sanad --no-create-home sanad

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

VOLUME /app

USER sanad
# RUN /usr/local/bin/python -m pip install -r requirements.txt
COPY . ./app

RUN cd /app/venv/app

CMD ["flask", "run"]

# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "{.venv}.{app}:webapp"]

