
# Modern API

Building secured API with `FastAPI` and `SQLModel`




## Installation

Install and running mapi with `poetry`

```bash
git clone https://github.com/Proteusiq/modernapi.git && cd modernapi
poetry install
invoke init-db
cd mapi
uvicorn main:app --reload  
```

# Project Direction
My desire is  to create a template that is simple and robust. 
Level access and admin power to CRUD users are next on my table. <br>
I welcome PR and any help to make this repository a starting point for building secured APIs.

# API
API swagger is running at `localhost:8000/docs`. <br>
Init DB added user `MrRobot` with `fsociety` as password. 

# TODO
* [ ] Add tests
* [X] Create Access Level [Admin, Visitor]
* [X] Create endpoint to add, update, and delete users 

    
