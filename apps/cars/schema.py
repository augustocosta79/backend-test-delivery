from datetime import datetime
import uuid
from ninja import Schema
from apps.users.schema import UserSchema

class CarSchema(Schema):
    id: uuid.UUID
    name: str
    year: int
    description: str
    sold: bool
    created: datetime


class CarCreateSchema(Schema):
    name: str
    year: int
    description: str
    sold: bool
    user_id: uuid.UUID