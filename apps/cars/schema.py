import uuid
from datetime import datetime
from typing import Optional

from ninja import Schema
from pydantic import Field


class CarSchema(Schema):
    id: uuid.UUID
    name: str = Field(..., min_length=1)
    year: int = Field(..., gt=0)
    description: str
    sold: bool
    created: datetime


class CarCreateSchema(Schema):
    name: str = Field(..., min_length=1)
    year: int = Field(..., gt=0)
    description: str
    sold: Optional[bool] = False
    user_id: uuid.UUID
