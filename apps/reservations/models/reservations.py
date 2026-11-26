from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from apps.base.models import (CreatedTimeStampModel,
                              CreatedAccountModel,
                              UpdatedTimeStampModel,
                              UpdatedAccountModel,
                              Status,
                              UUIDModel)
from apps.accounts.models import AccountModel
from apps.listings.models import ListingModel


class ReservationModel(UUIDModel,
                       CreatedTimeStampModel,
                       CreatedAccountModel,
                       UpdatedTimeStampModel,
                       UpdatedAccountModel,
                       models.Model):
    check_in = models.DateField(verbose_name=_('Дата заезда'))
    check_out = models.DateField(verbose_name=_('Дата выезда'))
    account = models.ForeignKey(AccountModel, on_delete=models.PROTECT, related_name='reservations')
    status = models.CharField(max_length=20,
                              choices=Status,
                              default=Status.PENDING,
                              verbose_name=_('Статус резервирования'), )
    listing = models.ForeignKey(ListingModel, on_delete=models.PROTECT, related_name='reservations', )
    total_amount = models.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0.01'))],
                                       verbose_name=_('Итоговая сумма резервирования'),
                                       )
    total_guests = models.PositiveIntegerField(default=1,
                                               verbose_name=_('Общее количество гостей'))

    class Meta:
        db_table = 'reservations'
        verbose_name = _('Резервирование')
        verbose_name_plural = _('Резервирования')
        ordering = ('-created_at',)
        constraints = [models.CheckConstraint(condition=models.Q(status__in=Status.values),
                                              name='%(app_label)s_%(class)s_status_valid',
                                              ),
                       models.CheckConstraint(condition=models.Q(total_amount__gt=0.01),
                                              name='total_amount_greater_1',
                                              )
                       ]
