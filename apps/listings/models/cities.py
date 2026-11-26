from django.db import models
from django.utils.translation import gettext_lazy as _
from .countries import CountryModel


class CityModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Название города'))
    country = models.ForeignKey(CountryModel,
                                on_delete=models.CASCADE,
                                related_name='cities',
                                verbose_name=_('Страна'))

    class Meta:
        db_table = 'cities'
        verbose_name = _('Город')
        verbose_name_plural = _('Города')
        ordering = ('title',)

    def __str__(self):
        return self.title
