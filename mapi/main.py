from fastapi import FastAPI
from api.routers import auth, user, status


app = FastAPI(
    title="Awesome API",
    description="Inspire By Prayson's Madness",
    version="0.0.1",
)


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(status.router)
