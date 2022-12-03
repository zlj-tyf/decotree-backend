from fastapi import APIRouter, Path, Response
from starlette.requests import Request

from api.tree.request.tree import (
    SaveTreeRequest,
)
from api.tree.response.tree import SaveTreeResponse
from app.user.services.tree import TreeService
from core.exceptions import BadRequestException

tree_router = APIRouter()


@tree_router.get(
    "/tree/{user_hash}",
    response_model=SaveTreeResponse,
)
async def get_tree(
    request: Request,
    user_hash: str = Path(title="최종 설문 완료 -> 중복 안되는 해시값 생성")
):
    tree = await TreeService().get_tree_by_user_hash(
        user_hash=user_hash,
    )
    return {"data": tree}


@tree_router.post(
    "/tree/{user_hash}",
    response_model=SaveTreeResponse,
)
async def save_tree_status(
    request: Request,
    body: SaveTreeRequest,
    user_hash: str = Path(title="최종 설문 완료 -> 중복 안되는 해시값 생성")
):
    tree = await TreeService().save_tree(
        user_hash=user_hash,
        tree_type=body.tree_type,
        brightness=body.brightness,
        has_santa=body.has_santa,
        weather=body.weather,
        song_type=body.song_type,
    )
    return {"data": tree}
