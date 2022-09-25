# start by pulling the python image
FROM python:3.8.5-slim-buster

EXPOSE 5000

WORKDIR /usr/src/app

# ENV PYTHONBUFFERED 1

# ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0


# RUN apt-get -y install build-essential
RUN /usr/local/bin/python -m pip install --upgrade pip

# RUN pip install markupsafe==1.1.1 flask
RUN /usr/sbin/groupadd -g 1000 sanad && /usr/sbin/useradd -g 1000 -r sanad

RUN apt-get update

RUN apt-get install -y default-libmysqlclient-dev libssl-dev tk && \
    apt-get install -y --no-install-recommends gcc python-dev

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

VOLUME /app

USER sanad
# RUN /usr/local/bin/python -m pip install -r requirements.txt
COPY . ./


# RUN cd myflask_project/venv/app

# CMD ["flask", "run"]

# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "{.venv}.{app}:webapp"]

