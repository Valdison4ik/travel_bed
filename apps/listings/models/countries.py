from django.db import models
from django.utils.translation import gettext_lazy as _


class CountryModel(models.Model):
    title = models.CharField(unique=True, max_length=100,verbose_name=_('Название страны'))

    class Meta:
        db_table = 'country'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ('title',)

    def __str__(self):
        return self.title


