from ninja import NinjaAPI, Redoc, Swagger

from apps.authentication.api import authentication_router
from apps.users.api import user_router
from apps.cars.api import car_router

docs = {
    "swagger": Swagger(),
    "redoc": Redoc()
}

api = NinjaAPI(
    csrf=False,
    title="API",
    version="1.0.0",
    description="This is a API to manage data",
    docs=docs["swagger"]
)


api.add_router("/auth", authentication_router, tags=["Authentication"])
api.add_router("/users", user_router, tags=["Users"])
api.add_router("/cars", car_router, tags=["Cars"])
