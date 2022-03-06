from fastapi import APIRouter
from mapi.models.heartbeat import HearbeatResult

router = APIRouter(
    prefix="/health",
    tags=["health"],
)


@router.get("/heartbeat", response_model=HearbeatResult, name="heartbeat")
def get_hearbeat() -> HearbeatResult:
    heartbeat = HearbeatResult(is_alive=True)
    return heartbeat
