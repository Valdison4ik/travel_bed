from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.base.models import (CreatedTimeStampMixin,
                              CreatedAccountMixin,
                              Status)
from apps.reservations.models import ReservationModel


class StatusLogModel(CreatedTimeStampMixin, CreatedAccountMixin, models.Model):
    """ Все статусы по резервированию с комментариями """
    status = models.CharField(max_length=20,
                              choices=Status,
                              default=Status.PENDING,
                              verbose_name=_('Статус резервирования'),
                              )
    reservation = models.ForeignKey(ReservationModel,
                                    on_delete=models.CASCADE,
                                    related_name='statuses',
                                    )
    status_comment = models.TextField(blank=True,
                                      null=True,
                                      verbose_name=_('Комментарий к статусу'))
    is_visible = models.BooleanField(default=False,
                                     verbose_name=_('Видимость комментария для Гостя'))

    class Meta:
        db_table = 'status_log'
        verbose_name = 'Status Log'
        verbose_name_plural = 'Status Logs'
        ordering = ('-created_at',)

    def __str__(self):
        return self.status
