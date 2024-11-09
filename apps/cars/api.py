import uuid
from typing import List

from apps.users.service import UserService
from ninja import Router
from utils.jwt import JWTAuth

from .schema import CarCreateSchema, CarSchema
from .service import CarService

car_router = Router(auth=JWTAuth())
# car_router = Router()
service = CarService()
user_service = UserService()


@car_router.get("/", response=List[CarSchema])
def list_cars(request):
    return service.list_cars()


@car_router.get("/{car_id}", response=CarSchema)
def get_car(request, car_id: uuid.UUID):
    return service.get_car(car_id)


@car_router.post("/", response=CarSchema)
def create_car(request, payload: CarCreateSchema):
    user = user_service.get_user_by_id(payload.user_id)
    return service.create_car(payload, user)
