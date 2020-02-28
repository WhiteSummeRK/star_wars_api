FROM python:3.7.1

LABEL Author="Kauan Alves"
LABEL E-mail="kauan.alves1996@gmail.com"
LABEL version="0.0.1"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "star_wars_api/api/app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ADD . /app

EXPOSE 5000

CMD flask run --host=0.0.0.0