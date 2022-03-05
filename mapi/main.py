from fastapi import FastAPI
from api.routers import auth, admin, user, status
from core.event_handlers import start_app_handler, stop_app_handler


app = FastAPI(
    title="Python Weekend API",
    description="Inspired By Prayson's Madness",
    version="0.0.2",
)


app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(user.router)
app.include_router(status.router)

app.add_event_handler("startup", start_app_handler(app))
app.add_event_handler("shutdown", stop_app_handler(app))
