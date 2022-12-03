from sqlalchemy import Boolean, Column, Integer, String

from core.db import Base


class Tree(Base):
    __tablename__ = "tree"

    id = Column(Integer, primary_key=True)
    user_hash = Column(String(200), index=True)
    tree_type = Column(String(20))
    brightness = Column(String(20))
    has_santa = Column(Boolean)
    weather = Column(String(20))
    song_type = Column(String(20))
    song_id = Column(Integer)
