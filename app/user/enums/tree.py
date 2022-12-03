import enum


class TreeTypeEnum(enum.Enum):
    family = "family"
    solo = "solo"
    friend = "friend"
    couple = "couple"
    coworker = "coworker"


class BrightnessLevelEnum(enum.Enum):
    brightest = "brightest"
    more_bright = "more_bright"
    normal = "normal"
    none = "none"


class WeatherEnum(enum.Enum):
    snow = "snow"
    rain = "rain"
    none = "none"


class SongTypeEnum(enum.Enum):
    kpop = "kpop"
    pop = "pop"
    ballad = "ballad"
    any = "any"
