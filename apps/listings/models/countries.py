from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Lower


class CountryModel(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('Название страны'))

    class Meta:
        db_table = 'countries'
        verbose_name = _('Страна')
        verbose_name_plural = _('Страны')
        ordering = ('title',)
        constraints = [models.UniqueConstraint(Lower('title'), name='unique_lower_title'),
                       ]

    def __str__(self):
        return self.title
