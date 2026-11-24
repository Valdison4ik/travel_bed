from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from apps.base.models import (CreatedTimeStampMixin,
                              CreatedAccountMixin,
                              UpdatedTimeStampMixin,
                              UpdatedAccountMixin,
                              UUIDModel)
from apps.listings.models import ListingModel


class ReservationModel(UUIDModel,
                       CreatedTimeStampMixin,
                       CreatedAccountMixin,
                       UpdatedTimeStampMixin,
                       UpdatedAccountMixin,
                       models.Model):
    check_in = models.DateField(verbose_name=_('Дата заезда'))
    check_out = models.DateField(verbose_name=_('Дата выезда'))
    listing = models.ForeignKey(ListingModel,
                                null=True,
                                on_delete=models.SET_NULL,
                                related_name='reservations',)
    total_amount = models.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0.00'))],
                                       verbose_name=_('Итоговая сумма брони'),
                                       )
    total_guests = models.PositiveIntegerField(default=1,
                                               verbose_name=_('Общее количество гостей'))

    class Meta:
        db_table = 'reservation'
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        ordering = ('-created_at',)
        # constraints = []