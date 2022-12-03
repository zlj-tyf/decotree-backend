from pydantic import BaseModel

from app.user.schemas.tree import TreeSchema


class SaveTreeResponse(BaseModel):
    data: TreeSchema

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "tree_type": "family",
                    "brightness": "brightest",
                    "has_santa": True,
                    "weather": "snow",
                    "song_type": "kpop",
                    "song_id": 1234123412,
                }
            }
        }
