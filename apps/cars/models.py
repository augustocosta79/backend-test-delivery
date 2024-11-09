from uuid import uuid4

from apps.users.models import CustomUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(_("name"), max_length=60)
    year = models.PositiveIntegerField(_("year"))
    description = models.TextField(_("description"))
    sold = models.BooleanField(_("sold"), default=False)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.year})"
