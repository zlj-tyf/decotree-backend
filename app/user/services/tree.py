from typing import Optional

from app.user.enums.tree import (
    BrightnessLevelEnum, SongTypeEnum, TreeTypeEnum,
    WeatherEnum,
)
from app.user.models.tree import Tree
from app.user.repositories.tree import TreeRepository
from app.user.schemas.tree import TreeSchema
from core.db import Transactional


class TreeService:
    def __init__(self):
        self.tree_repo = TreeRepository(Tree)

    async def get_tree_by_user_hash(self, user_hash: str) -> Optional[TreeSchema]:
        return await self.tree_repo.get_tree_by_user_hash(user_hash)

    @Transactional()
    async def save_tree(
        self,
        user_hash: str,
        tree_type: TreeTypeEnum,
        brightness: BrightnessLevelEnum,
        has_santa: bool,
        weather: WeatherEnum,
        song_type: SongTypeEnum,
    ) -> TreeSchema:
        return await self.tree_repo.save_tree(
            user_hash,
            tree_type,
            brightness,
            has_santa,
            weather,
            song_type,
        )
