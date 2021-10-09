
# Modern API

Building secured API with `FastAPI` and `SQLModel`




## Installation

Install mapi with `poetry`

```bash
git clone https://github.com/Proteusiq/modernapi.git && cd modernapi
poetry install
invoke init-db
cd mapi
uvicorn main:app --reload  
```

# API
API swagger is running at `localhost:8000/docs`. <br>
Init DB added user `MrRobot` with `fsociety` as password. 

# TODO
* [ ] Add tests
* [ ] Create Access Level [Admin, Normal, Semi]
* [ ] Create endpoint to add, update, and delete users 

    