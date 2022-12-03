from typing import Optional

from pydantic import BaseModel, Field

from app.user.enums.tree import (
    BrightnessLevelEnum, SongTypeEnum, TreeTypeEnum,
    WeatherEnum,
)


class TreeSchema(BaseModel):
    tree_type: TreeTypeEnum = Field(description="크리스마스 트리 타입")
    brightness: BrightnessLevelEnum = Field(description="트리 밝기 정도")
    has_santa: bool = Field(description="산타 데코 노출 여부")
    weather: WeatherEnum = Field(description="날씨 애니메이션 노출 여부")
    song_type: SongTypeEnum = Field(description="좋아하는 노래 유형")
    song_id: Optional[int] = Field(None, description="Apple Music id")

    class Config:
        orm_mode = True
