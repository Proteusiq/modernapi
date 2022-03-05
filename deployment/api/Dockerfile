FROM python:3.9.10-slim-bullseye

ARG DATABASE_URL
ARG USER=app

RUN groupadd $USER && useradd --no-log-init -r -g $USER $USER

WORKDIR /app



COPY ./deployment/api/requirements.txt ./
COPY ./mapi ./mapi

RUN pip install --upgrade pip \
    pip install -r requirements.txt 

COPY mapi/.env .env
RUN chown -R $user:$user /app

ENV DATABASE_URL=${DATABASE_URL:-'sqlite:///database.db'}
ENV PYTHONPATH mapi

USER $USER

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]