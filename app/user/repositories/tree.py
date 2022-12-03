from typing import Optional

from sqlalchemy import select

from app.user.enums.tree import (
    BrightnessLevelEnum, SongTypeEnum, TreeTypeEnum,
    WeatherEnum,
)
from app.user.models.tree import Tree
from app.user.schemas.tree import TreeSchema
from core.db import session
from core.repository.base import BaseRepo


class TreeRepository(BaseRepo):
    async def get_tree_by_user_hash(self, user_hash: str) -> Optional[TreeSchema]:
        query = select(self.model).where(self.model.user_hash == user_hash)
        tree = await session.execute(query)
        tree = tree.scalars().first()

        if not tree:
            return None
        return TreeSchema.from_orm(tree)

    async def save_tree(
        self,
        user_hash: str,
        tree_type: TreeTypeEnum,
        brightness: BrightnessLevelEnum,
        has_santa: bool,
        weather: WeatherEnum,
        song_type: SongTypeEnum,
        song_id: Optional[int] = None,
    ) -> TreeSchema:
        _model = Tree(
            user_hash=user_hash,
            tree_type=tree_type.value,
            brightness=brightness.value,
            has_santa=has_santa,
            weather=weather.value,
            song_type=song_type.value,
        )
        if song_id is not None:
            _model.song_id = song_id

        session.add(_model)
        await session.flush()
        return TreeSchema.from_orm(_model)
