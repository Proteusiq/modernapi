
# Modern API

Building secured API with `FastAPI` and `SQLModel` running behind `NGINX`




## Installation

Running mapi with `docker` to get FastAPI behind Nginx as a proxy

```bash
git clone https://github.com/Proteusiq/modernapi.git && cd modernapi
docker-compose up -d

# head to http://localhost/docs on the browser
# run below to take it down
# docker-compose down
```

Running mapi with `invoke`

```bash
poetry install
invoke app

# head to http://localhost:8000/docs
```



# Project Direction
My desire is to create a template that is simple and robust.
* ~~Level access and admin power to CRUD users are next on my table~~.
* Using Postgres as a database [most likely a branch - postgress]
* Using Celery as background executor [most likely a branch - celery]

### Similiar Project with Extras:pre=[init_db]
[FastAPI + Postgres: Creator of FastAPI = Sebastian](https://github.com/tiangolo/full-stack-fastapi-postgresql) - Superior to this project :D <br>
[AuthX](https://github.com/yezz123/AuthX) - Ready to use and customisable Authentications and Authorisation management for FastAPI ⚡

I welcome PR and any help to make this repository a starting point for building secured APIs.

# API
API swagger is running at `localhost/docs`. <br>
Init DB added user `MrRobot` with `fsociety` as password.

# TODO
* [ ] Add tests
* [X] Create Access Level [Admin, Visitor]
* [X] Create endpoint to add, update, and delete users
* [ ] Replace prints with logging
* [ ] Add a simple Admin UI
* [ ] Allow None Admin to change their fullname, email and password
* [ ] Add strong password and email validation with Pydantic
* [ ] Terraform deployment \w and ~\w Kubernetes on Azure, AWS and GCP
