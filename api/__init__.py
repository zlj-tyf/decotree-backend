from fastapi import APIRouter

from api.tree.tree import tree_router

router = APIRouter()
router.include_router(tree_router, prefix="/tree", tags=["Tree"])


__all__ = ["router"]
