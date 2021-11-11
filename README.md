
# Modern API

Building secured API with `FastAPI` and `SQLModel`




## Installation

Install and running mapi with `poetry`. Invoke will create a temporary sqliteDB
and delete it with app tear down. 

```bash
git clone https://github.com/Proteusiq/modernapi.git && cd modernapi
poetry install
invoke app
```

# Project Direction
My desire is  to create a template that is simple and robust. 
* ~~Level access and admin power to CRUD users are next on my table~~.
* Using Postgres as a database [most likely a branch - postgress]
* Using Celery as background executor [most likely a brance - celery]

### Similiar and Superior Project:
[AuthX](https://github.com/yezz123/AuthX)

I welcome PR and any help to make this repository a starting point for building secured APIs.

# API
API swagger is running at `localhost:8000/docs`. <br>
Init DB added user `MrRobot` with `fsociety` as password. 

# TODO
* [ ] Add tests
* [X] Create Access Level [Admin, Visitor]
* [X] Create endpoint to add, update, and delete users
* [ ] Allow None Admin to change their fullname, email and password
* [ ] Add strong password and email validation with Pydantic

    
