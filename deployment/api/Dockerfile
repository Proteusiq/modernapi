FROM python:3.9.10-slim-bullseye

ARG DATABASE_URL
ARG USER=app

RUN groupadd $user && useradd --no-log-init -r -g $user $user

WORKDIR /app



COPY requirements.txt ./
COPY mapi ./mapi

RUN pip install --upgrade pip \
    pip install -r requirements.txt 

COPY .env .env
RUN chown -R $user:$user /app

ENV DATABASE_URL=${DATABASE_URL:-'http:///sqlite.db'}
ENV PYTHONPATH mapi

USER $USER

EXPOSE 8000