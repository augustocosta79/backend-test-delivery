from http import HTTPStatus
from typing import List
from uuid import UUID

from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from utils.pdf import PdfService

from .models import Car


# Create your views here.
class CarService:
    @staticmethod
    def get_car_by_id(car_id: UUID) -> Car:
        return get_object_or_404(Car, id=car_id)

    @staticmethod
    def get_all_cars() -> List[Car]:
        return Car.objects.all()

    def get_car(self, car_id: UUID) -> Car:
        if not (car := self.get_car_by_id(car_id=car_id)):
            raise HttpError(HTTPStatus.NOT_FOUND, "Carro não encontrado")
        return car

    def create_car(self, payload, user) -> Car:
        new_car = Car(
            name=payload.name,
            year=payload.year,
            description=payload.description,
            sold=payload.sold,
            user=user,
        )
        new_car.save()

        pdf_file = PdfService.generate_car_pdf(new_car)

        # Send email with attachment
        email = EmailMessage(
            subject="New Car Added",
            body=f"A new car has been added: {new_car.name} ({new_car.year})",
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_TO_ADDRESS],
        )
        email.attach("car_details.pdf", pdf_file, "application/pdf")
        email.send(fail_silently=False)

        return new_car

    def list_cars(self) -> List[Car]:
        if not (cars := self.get_all_cars()):
            raise HttpError(HTTPStatus.NOT_FOUND, "Não há carros para retornar")
        return cars
