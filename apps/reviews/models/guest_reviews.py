from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

from apps.base.models import (CreatedTimeStampModel,
                              CreatedAccountModel,
                              UpdatedTimeStampModel,
                              UpdatedAccountModel)
from apps.reservations.models import ReservationModel


class GuestReviewModel(CreatedTimeStampModel, CreatedAccountModel,
                       UpdatedTimeStampModel, UpdatedAccountModel,
                       models.Model):
    reservation = models.OneToOneField(ReservationModel,
                                       on_delete=models.PROTECT,
                                       related_name='review'
                                       )
    grade = models.PositiveSmallIntegerField(verbose_name=_('Оценка гостя'),
                                             validators=[MinValueValidator(1), MaxValueValidator(5)]
                                             )
    comment = models.TextField(blank=True, verbose_name=_('Отзыв гостя'), )
    is_published = models.BooleanField(default=True, verbose_name=_('Публиковать ли отзыв '), )

    class Meta:
        db_table = 'guest_reviews'
        verbose_name = _('Отзыв гостя')
        verbose_name_plural = _('Отзывы гостей')
        ordering = ['-created_at']
        constraints = [models.CheckConstraint(condition=models.Q(grade__gte=1, grade__lte=5),
                                              name='grade_between_1_and_5',
                                              )
                       ]

    def __str__(self):
        return f'{self.grade} - {self.comment}'
