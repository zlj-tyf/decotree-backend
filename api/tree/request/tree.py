from pydantic import BaseModel, Field

from app.user.enums.tree import SongTypeEnum


class TreeRequest(BaseModel):
    user_hash: str = Field(str, description="공유하기 버튼 클릭 -> 중복 안되는 해시값")


class TreeSongRequest(BaseModel):
    song_type: SongTypeEnum = Field(
        description="어떤 노래를 듣고 싶으신가요 -> Enum string"
    )
