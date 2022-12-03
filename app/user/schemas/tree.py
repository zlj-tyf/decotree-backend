from pydantic import BaseModel

from app.user.enums.tree import BrightnessLevelEnum, TreeTypeEnum, WeatherEnum


class TreeStatus(BaseModel):
    tree_type: TreeTypeEnum
    brightness: BrightnessLevelEnum
    has_santa: bool
    weather: WeatherEnum

