from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
# from django.contrib.gis.db import models as geomodels
from django.utils.translation import gettext_lazy as _

from apps.base.models import (CreatedTimeStampMixin,
                              CreatedAccountMixin,
                              UpdatedTimeStampMixin,
                              UpdatedAccountMixin,
                              SoftDeleteModel,
                              HousingType,
                              UUIDModel)
from .cities import CityModel


class ListingModel(UUIDModel,
                   CreatedTimeStampMixin, CreatedAccountMixin,
                   UpdatedTimeStampMixin, UpdatedAccountMixin,
                   SoftDeleteModel
                   ):
    """ Объявления об аренде """
    title = models.CharField(max_length=100, verbose_name=_('Заголовок объявления'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Описание объявления'))
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE,related_name='listings',)

    # location = geomodels.PointField(verbose_name=_('Гео-координаты объекта'))
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name=_('Координата широты'))
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name=_('Координата долготы'))

    housing_type = models.CharField(max_length=15,choices=HousingType,verbose_name=_('Тип объекта'),)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.00'))],
                                verbose_name=_('Цена за одну ночь'),
                                )

    class Meta:
        db_table = 'listing'
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'
        ordering = ('-created_at',)
        # constraints = []

    def __str__(self):
        return self.title
