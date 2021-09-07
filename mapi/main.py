from fastapi import FastAPI, File, UploadFile

from celery.result import AsyncResult
from worker import do_this  # to minio

app = FastAPI(title="Awesome API")


@app.get("/")
def home():
    return {"message": "home sweet home!"}


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
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
