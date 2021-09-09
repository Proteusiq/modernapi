from fastapi import FastAPI, Request, File, UploadFile, Depends
from models import models
from database.configuration import engine
from core import user, auth
from celery.result import AsyncResult
from worker import do_this  # to minio

app = FastAPI(
    title="Awesome API",
    description="Heavly DodgeAPI",
    version="0.0.1",
)


app.include_router(auth.router)
app.include_router(user.router)


@app.get("/")
async def index(request: Request):
    return {"request": request}


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile = File(...),
    authenticated: bool = Depends(...),
):
    # minio.delay(file)
    return {"filename": file.filename}


@app.get("/go/{snooze}")
def go(snooze: int):
    task = do_this.delay(snooze)
    return {"task_id": task.id}


@app.get("/result/{task_id}")
def go_results(task_id: str):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return result
