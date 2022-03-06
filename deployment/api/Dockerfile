FROM python:3.9.10-slim-bullseye

ARG USER=app

RUN groupadd $USER && useradd --no-log-init -r -g $USER $USER

WORKDIR /app

COPY ./deployment/api/requirements.txt ./

RUN pip install --upgrade pip \
    pip install -r requirements.txt 

COPY ./mapi ./mapi
COPY ./deployment/api/.env.example .env
RUN chown -R $user:$user /app

ENV PYTHONPATH mapi

USER $USER

EXPOSE 8000

CMD ["gunicorn", "mapi.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]