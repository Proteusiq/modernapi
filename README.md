
# Modern API

Building secured API with `FastAPI` and `SQLModel` running behind `NGINX`




## Installation

Running mapi with `docker`. 

```bash
git clone https://github.com/Proteusiq/modernapi.git && cd modernapi
docker-compose up -d

# run below to take it down
# docker-compose down
```

Running mapi with `invoke`

```bash
poetry install
invoke app
```



# Project Direction
My desire is  to create a template that is simple and robust. 
* ~~Level access and admin power to CRUD users are next on my table~~.
* Using Postgres as a database [most likely a branch - postgress]
* Using Celery as background executor [most likely a brance - celery]

### Similiar Project with Extras:pre=[init_db]
[AuthX](https://github.com/yezz123/AuthX) - Ready to use and customizable Authentications and Authorisation management for FastAPI ⚡

I welcome PR and any help to make this repository a starting point for building secured APIs.

# API
API swagger is running at `localhost/docs`. <br>
Init DB added user `MrRobot` with `fsociety` as password. 

# TODO
* [ ] Add tests
* [X] Create Access Level [Admin, Visitor]
* [X] Create endpoint to add, update, and delete users
* [ ] Replace prints with logging
* [ ] Allow None Admin to change their fullname, email and password
* [ ] Add strong password and email validation with Pydantic

    
