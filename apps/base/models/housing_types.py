from django.db import models
from django.utils.translation import gettext_lazy as _


class HousingType(models.TextChoices):
    APARTMENT = 'apartment', _('Квартира')
    HOUSE = 'house', _('Дом / Коттедж')
    ROOM = 'room', _('Комната')
    SPECIALTY = 'specialty', _('Нестандартный формат')
