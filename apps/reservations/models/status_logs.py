from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.base.models import (CreatedTimeStampModel,
                              CreatedAccountModel,
                              Status)
from apps.reservations.models import ReservationModel


class StatusLogModel(CreatedTimeStampModel, CreatedAccountModel, models.Model):
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
        db_table = 'status_logs'
        verbose_name = _('Лог статуса')
        verbose_name_plural = _('Логи статусов')
        ordering = ('-created_at',)
        constraints = [models.CheckConstraint(condition=models.Q(status__in=Status.values),
                                              name='%(app_label)s_%(class)s_status_valid',
                                              )
                       ]

    def __str__(self):
        return self.status
