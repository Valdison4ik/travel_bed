from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

from apps.base.models import (CreatedTimeStampMixin,
                              CreatedAccountMixin,
                              UpdatedTimeStampMixin,
                              UpdatedAccountMixin)
from apps.reservations.models import ReservationModel
from apps.listings.models import ListingModel

rating_validators = [MinValueValidator(1), MaxValueValidator(5)]


class GuestReviewModel(CreatedTimeStampMixin, CreatedAccountMixin,
                        UpdatedTimeStampMixin, UpdatedAccountMixin,
                        models.Model):
    reservation = models.OneToOneField(ReservationModel,
                                       on_delete=models.CASCADE,
                                       related_name='review'
                                       )
    listing = models.ForeignKey(ListingModel,
                                on_delete=models.CASCADE,
                                related_name='reviews'
                                )
    rating = models.PositiveSmallIntegerField(verbose_name=_('Оценка гостя'),
                                              validators=rating_validators
                                              )
    # cleanliness_rating = models.PositiveSmallIntegerField(validators=rating_validators, null=True, blank=True)
    # communication_rating = models.PositiveSmallIntegerField(validators=rating_validators, null=True, blank=True)
    # location_rating = models.PositiveSmallIntegerField(validators=rating_validators, null=True, blank=True)
    comment = models.TextField(blank=True, verbose_name=_('Отзыв гостя'), )
    # host_reply = models.TextField(blank=True)
    # replied_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name=_('Публиковать ли отзыв '), )

    class Meta:
        db_table = 'guest_review'
        verbose_name = _('Отзыв гостя')
        verbose_name_plural = _('Отзывы гостей')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.rating} - {self.comment}'
