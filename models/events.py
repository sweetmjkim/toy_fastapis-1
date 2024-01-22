from typing import Optional, List

from beanie import Document
from pydantic import BaseModel

# 개발자 실수로 들어가는 field 제한
class Event(Document):
    creator: Optional[str]
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Settings:
        name = "events"
